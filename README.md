# Клиент Blockfield

<img src="assets/icon.png" alt="Blockfield" width="64" height="64" />

Готовая клиентская сборка для игры на `play.blockfield.pro`: Minecraft 1.21.1, Fabric и Java 21.

[Скачать клиент](https://github.com/Blockfield/blockfield-releases/releases/latest) ·
[Сайт](https://blockfield.pro)

## Выберите способ установки

**[Blockfield Launcher](https://github.com/Blockfield/Blockfield-Launcher)** сам установит Java, Minecraft, Fabric и модпак, а затем будет обновлять сборку. Доступен для Windows, Linux и Mac — Intel и Apple Silicon.

Если используете другой лаунчер, скачайте подходящий дистрибутив:

| Дистрибутив           | Для чего                                    | Скачать                                                                                                                   |
| :-------------------- | :------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------ |
| **Prism Launcher**    | Готовый инстанс с обновлением через packwiz | [Blockfield-prism.zip](https://github.com/Blockfield/blockfield-releases/releases/latest/download/Blockfield-prism.zip)   |
| **Modrinth**          | Импорт в лаунчер с поддержкой `.mrpack`     | [Blockfield.mrpack](https://github.com/Blockfield/blockfield-releases/releases/latest/download/Blockfield.mrpack)         |
| **Полный клиент**     | Ручная установка модов и конфигурации       | [Blockfield-client.zip](https://github.com/Blockfield/blockfield-releases/releases/latest/download/Blockfield-client.zip) |
| **Контрольные суммы** | Проверка целостности скачанных файлов       | [SHA256SUMS](https://github.com/Blockfield/blockfield-releases/releases/latest/download/SHA256SUMS)                       |

Все версии и заметки к ним находятся в [Releases](https://github.com/Blockfield/blockfield-releases/releases). Этот репозиторий хранит готовые клиентские сборки и обращения игроков.

## Подключение

|                     |                                                               |
| :------------------ | :------------------------------------------------------------ |
| **Сервер**          | `play.blockfield.pro`                                         |
| **Minecraft**       | `1.21.1` · Fabric                                             |
| **Java**            | `21` — официальный лаунчер установит её автоматически         |
| **Память для игры** | Начните с 4 ГБ; оставьте память для ОС и остальных приложений |

<details>
<summary><b>Установка в Prism Launcher</b></summary>

1. Скачайте `Blockfield-prism.zip`.
2. В Prism выберите «Добавить сборку → Импорт» и укажите архив.
3. Выберите Java 21 и выделите память для игры.
4. Запустите инстанс: packwiz проверит и обновит моды перед стартом.

</details>

<details>
<summary><b>Импорт .mrpack</b></summary>

Импортируйте `Blockfield.mrpack` в лаунчер с поддержкой этого формата и дождитесь установки. Для игры нужна Java 21. Адрес сервера — `play.blockfield.pro`.

</details>

<details>
<summary><b>Ручная установка</b></summary>

Создайте отдельный инстанс Minecraft 1.21.1 с Fabric и Java 21. Распакуйте `Blockfield-client.zip` в папку этого инстанса. Не смешивайте сборку с модами другого профиля. При следующем релизе ручную установку потребуется обновить самостоятельно.

</details>

<details>
<summary><b>Проверка целостности</b></summary>

Скачайте `SHA256SUMS` из того же релиза и сравните указанную сумму с вычисленной:

```sh
# Linux
sha256sum Blockfield-client.zip

# macOS
shasum -a 256 Blockfield-client.zip
```

```powershell
# Windows
Get-FileHash Blockfield-client.zip -Algorithm SHA256
```

</details>

## Поддержка

[Сообщить об ошибке клиента](https://github.com/Blockfield/blockfield-releases/issues) · [Ошибка лаунчера](https://github.com/Blockfield/Blockfield-Launcher/issues)

Укажите версию сборки, ОС, способ установки и шаги воспроизведения. При сбое приложите `logs/latest.log` или отчёт из `crash-reports/`, предварительно удалив личные данные и токены.

Моды и ресурсы в составе сборки сохраняют лицензии своих авторов. Публичная загрузка сборки сама по себе не меняет эти условия.

## Developer checks

Install Python 3.12+, Node.js 22 and Just 1.57.0 on Linux or Windows. Quality tools stay in the project cache.

```sh
just setup
just check
just format
```

`just --list` lists supported build and application commands.

Условия использования: [LICENSE](LICENSE).
