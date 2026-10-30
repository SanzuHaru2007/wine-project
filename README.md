# 🍷 Wine Quality Telegram Bot

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Telebot](https://img.shields.io/badge/Telebot-pyTelegramBotAPI-green.svg)
![SQLite](https://img.shields.io/badge/Database-SQLite3-lightgrey.svg)

Интерактивный Telegram-бот, который выдает случайные характеристики красного вина из датасета **Red Wine Quality**.

---

## 📌 О проекте

Бот позволяет пользователю в один клик получить случайную карточку вина с его физико-химическими свойствами и оценкой качества.

### 📊 Выводимые характеристики:
* **Кислотность (fixed acidity)** — уровень фиксированной кислотности.
* **Алкоголь (alcohol)** — процентное содержание алкоголя.
* **Качество (quality)** — оценка качества по 10-балльной шкале.

---

## 🛠 Технологический стек

* **Язык:** Python 3.x
* **Библиотека бота:** `pyTelegramBotAPI` (`telebot`)
* **База данных:** SQLite3 (таблица `red_wine`)

---

## 📂 Структура проекта

```text
wine-project/
├── config.py             # Конфигурационный файл (токен бота, имя БД)
├── logic.py              # Менеджер работы с базой данных SQLite
├── main.py               # Основной скрипт запуска бота и обработки команд
└── winequality-red.db    # База данных с датасетом вин
```

---

## 🚀 Быстрый запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/SanzuHaru2007/wine-project.git
cd wine-project
```

### 2. Установка зависимостей
Убедитесь, что у вас установлен Python, и установите библиотеку `pyTelegramBotAPI`:
```bash
pip install pytelegrambotapi
```

### 3. Настройка конфигурации
Откройте файл `config.py` и укажите ваш токен Telegram-бота (полученный у [@BotFather](https://t.me/BotFather)):
```python
TOKEN = 'ВАШ_TELEGRAM_TOKEN'
DATABASE = 'winequality-red.db'
```

> ⚠️ **Важно:** Не загружайте настоящий секретный токен в публичный репозиторий GitHub!

### 4. Запуск бота
```bash
python main.py
```

---

## 💻 Использование

1. Найдите вашего бота в Telegram и отправьте команду `/start`.
2. Нажмите на инлайн-кнопку **«Выбрать вино ->»**.
3. Бот пришлет случайную карточку с характеристиками вина и предложит выбрать еще!