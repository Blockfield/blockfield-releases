"""Protect the local tooling used by this repository's publication checks."""

import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import quality  # noqa: E402
import toolchain  # noqa: E402


class PinnedToolsTest(unittest.TestCase):
    def test_cached_download_is_verified_without_network(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "tool.bin"
            target.write_bytes(b"verified tool")
            checksum = hashlib.sha256(target.read_bytes()).hexdigest()
            with (
                patch.object(toolchain, "CACHE", Path(directory)),
                patch.object(toolchain.urllib.request, "urlopen") as request,
            ):
                self.assertEqual(
                    toolchain.download(target.name, "unused", checksum), target
                )
                request.assert_not_called()
                target.write_bytes(b"modified tool")
                with self.assertRaisesRegex(RuntimeError, "checksum mismatch"):
                    toolchain.download(target.name, "unused", checksum)
                request.assert_not_called()

    def test_failed_download_does_not_enter_the_cache(self):
        with tempfile.TemporaryDirectory() as directory:
            with (
                patch.object(toolchain, "CACHE", Path(directory)),
                patch.object(toolchain.urllib.request, "urlopen") as request,
            ):
                request.return_value.__enter__.return_value.read.return_value = b"wrong"
                with self.assertRaisesRegex(RuntimeError, "checksum mismatch"):
                    toolchain.download(
                        "tool.bin", "https://example.invalid/tool", "0" * 64
                    )
                self.assertFalse((Path(directory) / "tool.bin").exists())

    def test_child_environment_rejects_injected_runtime_options(self):
        injected = {
            key: "untrusted"
            for key in ("PYTHONPATH", "PYTHONHOME", "JAVA_TOOL_OPTIONS", "CLASSPATH")
        }
        with patch.dict(toolchain.os.environ, injected):
            env = toolchain.child_env()
        for key in injected:
            self.assertNotIn(key, env)
        self.assertEqual(env["PYTHONUTF8"], "1")

    def test_formatter_batches_keep_unicode_paths_and_limit_windows_arguments(self):
        files = [f"docs/space & $literal {index} \U0001f680.md" for index in range(400)]
        batches = list(quality.batches(files))
        self.assertGreater(len(batches), 1)
        self.assertEqual([name for batch in batches for name in batch], files)
        for batch in batches:
            self.assertLessEqual(
                sum(len(name.encode("utf-16-le")) // 2 + 3 for name in batch), 5000
            )


if __name__ == "__main__":
    unittest.main()
