<div align="center">

<img src="assets/icon.png" alt="Blockfield Logo" width="128" height="128" />

# BLOCKFIELD CLIENT DISTRIBUTIONS
### Официальные клиентские сборки и модпаки тактического PvP-проекта Blockfield

*«Высадка. Захват. Доминация.»*

[![Latest Release](https://img.shields.io/github/v/release/netherg-io/blockfield-releases?label=Релиз&style=for-the-badge&color=2ea44f)](https://github.com/netherg-io/blockfield-releases/releases)
[![Minecraft](https://img.shields.io/badge/Minecraft-1.21.1%20Fabric-orange?style=for-the-badge)](https://fabricmc.net/)
[![Java](https://img.shields.io/badge/Java-21%20%2F%20Temurin-red?style=for-the-badge)](https://adoptium.net/)
[![Launcher](https://img.shields.io/badge/Официальный%20Лаунчер-Windows%20%7C%20Linux-blue?style=for-the-badge)](https://github.com/netherg-io/blockfield-launcher-releases)
[![Formats](https://img.shields.io/badge/Форматы-mrpack%20%7C%20Prism%20%7C%20ZIP-brightgreen?style=for-the-badge)](https://github.com/netherg-io/blockfield-releases/releases)

<br />

[**📥 Скачать клиент**](#-клиентские-сборки-и-загрузка) • [**О проекте**](#-о-проекте-blockfield) • [**Инструкции по установке**](#-инструкции-по-установке) • [**Требования**](#-системные-требования) • [**Целостность**](#-проверка-целостности-sha-256) • [**Поддержка**](#-поддержка)

</div>

---

## 🚀 Клиентские сборки и загрузка

В данном репозитории публикуются официальные клиентские дистрибутивы и модпаки проекта **Blockfield**, собранные и верифицированные в рамках автоматизированного CI/CD пайплайна.

> [!IMPORTANT]
> **Рекомендуемый способ игры — [Blockfield Launcher](https://github.com/netherg-io/blockfield-launcher-releases).**  
> Официальный лаунчер на базе Tauri 2 и Rust обеспечивает максимальное быстродействие, автоматически настраивает подходящую среду Java, проверяет целостность файлов и моментально обновляет моды в один клик.  
> Если вы предпочитаете сторонние лаунчеры (Prism Launcher, Modrinth App, MultiMC) или ручную установку, выберите один из вариантов ниже.

| Формат / Пакет | Файл | Назначение / Лаунчер | Ссылка на загрузку |
| :--- | :--- | :--- | :--- |
| **Официальный лаунчер** | `.exe` / `.AppImage` / `.deb` / `.rpm` | Рекомендуемый автономный лаунчер со встроенной средой Java и автообновлениями | [**Скачать лаунчер**](https://github.com/netherg-io/blockfield-launcher-releases/releases/latest) |
| **Prism Launcher / MultiMC** | `Blockfield-prism.zip` | Готовый импортируемый инстанс с автоматической синхронизацией модов через Packwiz Bootstrap | [**Скачать ZIP**](https://github.com/netherg-io/blockfield-releases/releases/latest/download/Blockfield-prism.zip) |
| **Modrinth Modpack** | `Blockfield.mrpack` | Стандартный пакет Modrinth для Modrinth App, Prism Launcher, ATLauncher | [**Скачать mrpack**](https://github.com/netherg-io/blockfield-releases/releases/latest/download/Blockfield.mrpack) |
| **Полный архив клиента** | `Blockfield-client.zip` | Полный набор модов, конфигов и настроек для ручной распаковки в директорию `.minecraft` | [**Скачать ZIP**](https://github.com/netherg-io/blockfield-releases/releases/latest/download/Blockfield-client.zip) |
| **Контрольные суммы** | `SHA256SUMS` | Криптографические хеши SHA-256 для проверки целостности загруженных файлов | [**Страница Releases**](https://github.com/netherg-io/blockfield-releases/releases) |

> [!TIP]
> Все версии сборок, списки изменений и сопутствующие файлы доступны на странице [**Releases**](https://github.com/netherg-io/blockfield-releases/releases).

---

## 🎯 О проекте Blockfield

**Blockfield** — это масштабный тактический командный PvP-проект на базе **Minecraft (1.21.1 Fabric)**:

- 🚩 **Контроль секторов**: динамический захват и тактическое удержание стратегических рубежей.
- 🎖️ **6 специализированных классов**: штурмовик, снайпер, медик, инженер, поддержка и разведчик — каждый со своим снаряжением и способностями.
- 🚜 **Военная техника**: бронемашины и транспортные средства для быстрой переброски бойцов и огневого прикрытия.
- ⚡ **Операция «Железный фронт»**: уникальные театры военных действий, динамические фронтовые зоны и слаженная командная координация.
- 🌐 **Публичный игровой сервер**: `play.blockfield.pro:25565`

---

## 📦 Инструкции по установке

<details open>
<summary><b>1. Prism Launcher / MultiMC (Рекомендуемый альтернативный способ)</b></summary>

Сборка `Blockfield-prism.zip` содержит преднастроенный инстанс с предстартовым модулем **Packwiz Bootstrap**. При каждом запуске лаунчер автоматически проверяет актуальность модов на сервере обновлений и подключается к игровому серверу.

1. Установите [Prism Launcher](https://prismlauncher.org/) (или MultiMC).
2. Скачайте [**Blockfield-prism.zip**](https://github.com/netherg-io/blockfield-releases/releases/latest/download/Blockfield-prism.zip).
3. В Prism Launcher нажмите **«Добавить сборку»** (*Add Instance*) → **«Импорт»** (*Import*) → выберите скачанный `.zip`.
4. В свойствах инстанса убедитесь, что установлена **Java 21** и выделено от **4 ГБ ОЗУ**.
5. Запустите инстанс — моды обновятся автоматически, после чего откроется игра с подключением к серверу.

</details>

<details>
<summary><b>2. Modrinth App / лаунчеры с поддержкой .mrpack</b></summary>

1. Скачайте [**Blockfield.mrpack**](https://github.com/netherg-io/blockfield-releases/releases/latest/download/Blockfield.mrpack).
2. В Modrinth App нажмите **«Import from file»** / перетащите `.mrpack` в окно приложения.
3. Дождитесь окончания автоматической загрузки всех модов.
4. Адрес сервера для подключения: `play.blockfield.pro:25565`.

</details>

<details>
<summary><b>3. Ручная установка (Стандартный .minecraft)</b></summary>

1. Установите клиент **Minecraft 1.21.1**.
2. Установите [Fabric Loader 1.21.1](https://fabricmc.net/use/installer/) (версия загрузчика 0.16.x+).
3. Скачайте архив [**Blockfield-client.zip**](https://github.com/netherg-io/blockfield-releases/releases/latest/download/Blockfield-client.zip).
4. Распакуйте файлы архива в каталог `.minecraft` (`%appdata%\.minecraft` на Windows или `~/.minecraft` на Linux).
5. Запустите профиль Fabric 1.21.1 и подключитесь к серверу `play.blockfield.pro:25565`.

</details>

---

## 💻 Системные требования

| Параметр | Минимальные | Рекомендуемые |
| :--- | :--- | :--- |
| **Операционная система** | Windows 10/11 (64-bit), Linux, macOS | Windows 10/11 (64-bit), современный Linux |
| **Среда выполнения Java** | Java 21 (Temurin 21) | Java 21 LTS (Temurin 21) |
| **Процессор** | 2 ядра / 4 потока (Intel / AMD) | 4+ ядра (Intel Core i5 / Ryzen 5+) |
| **Оперативная память** | 4 ГБ ОЗУ (3 ГБ выделено в лаунчере) | 8+ ГБ ОЗУ (4–6 ГБ выделено в лаунчере) |
| **Видеокарта** | Поддержка OpenGL 4.4 / Vulkan | Дискретная видеокарта NVIDIA / AMD / Intel Arc |
| **Место на диске** | ~3 ГБ свободного места | SSD, от 5 ГБ свободного места |
| **Подключение к сети** | Широкополосный доступ в интернет | Стабильное соединение с низким пингом |

---

## 🔒 Проверка целостности (SHA-256)

Для проверки подлинности и целостности скачанных клиентских пакетов используйте контрольные суммы из файла `SHA256SUMS`:

```bash
# Linux / macOS
sha256sum -c SHA256SUMS --ignore-missing

# Windows (PowerShell)
Get-FileHash Blockfield-client.zip -Algorithm SHA256
```

---

## ❓ Часто задаваемые вопросы

<details>
<summary><b>Какая версия Java требуется для игры?</b></summary>
Для работы клиента требуется <b>Java 21</b> (рекомендуется <a href="https://adoptium.net/">Eclipse Temurin 21 LTS</a>). Если вы используете официальный <a href="https://github.com/netherg-io/blockfield-launcher-releases">Blockfield Launcher</a>, среда Java скачивается и настраивается автоматически.
</details>

<details>
<summary><b>Какой IP-адрес игрового сервера?</b></summary>
Основной публичный сервер проекта: <code>play.blockfield.pro:25565</code>. В официальном лаунчере и инстансе Prism он преднастроен по умолчанию.
</details>

<details>
<summary><b>Как получать обновления модов при выходе патчей?</b></summary>
В официальном лаунчере и в сборке для Prism Launcher обновления скачиваются автоматически перед каждым запуском. При ручной установке необходимо скачать свежий <code>Blockfield-client.zip</code> и обновить папку <code>mods/</code>.
</details>

<details>
<summary><b>Куда обращаться при возникновении ошибок или крашей?</b></summary>
Если вы столкнулись с ошибкой в работе клиента, откройте обращение в разделе <a href="https://github.com/netherg-io/blockfield-releases/issues">Issues</a> с описанием проблемы и прикрепите файл логов <code>logs/latest.log</code> или отчет о сбое <code>crash-reports/</code>.
</details>

---

## 💬 Поддержка

- **Баг-трекер**: [GitHub Issues](https://github.com/netherg-io/blockfield-releases/issues)
- **Официальный лаунчер**: [Blockfield Launcher](https://github.com/netherg-io/blockfield-launcher-releases)

---

<div align="center">

**[Blockfield Project](https://github.com/netherg-io)** • 2026

</div>
