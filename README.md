# 🤖 Artificial Support Bot

Bot name on telegram: AI Assistant Bot

An interactive Telegram portfolio bot built with **Python**, **FastAPI**, and the **Telegram Bot API**.

The bot serves as a personal portfolio, allowing users to explore my profile, projects, GitHub repositories, CV, and future work through an intuitive button-based interface.

## 🚀 Features

### 👨 About Me

* Personal introduction
* Background information
* Quick overview of skills and interests

### 📄 CV Access

* View and open my latest CV directly from Telegram
* Integrated with Google Drive

### 🚀 Projects Showcase

* Medical Record Management System
* Inventory Management System
* Car Rental Booking System

Each project includes:

* Description
* Technology stack
* GitHub repository
* Live demo link

### 💻 GitHub Integration

Quick access to my GitHub profile and repositories.

### 🌐 Portfolio Integration

Portfolio website support (coming soon).

## 🛠 Tech Stack

### Backend

* Python
* FastAPI

### Bot Integration

* Telegram Bot API
* Webhooks

### Development Tools

* Ngrok
* Git
* GitHub

## 📂 Project Structure

```text
telegram-ai-bot/
│
├── main.py
├── menus.py
│
├── handlers/
│   ├── about.py
│   └── projects.py
│
├── data/
│   ├── about.txt
│   ├── cv_link.txt
│   ├── github.txt
│   ├── portfolio.txt
│   └── projects/
│       ├── project_mrms.txt
│       ├── project_ims.txt
│       └── project_car_rental.txt
│
└── utils/
    ├── file_reader.py
    └── telegram.py
```

## 🔄 Workflow

```text
User
  ↓
Telegram
  ↓
Webhook
  ↓
FastAPI Backend
  ↓
Callback Router
  ↓
Handlers
  ↓
Response Sent Back To Telegram
```

## 📸 Current Navigation

```text
🏠 Main Menu
│
├── 👨 About Me
│   ├── 📄 Open CV
│   └── ⬅ Back
│
├── 🚀 Projects
│   ├── 🏥 MRMS
│   ├── 📦 IMS
│   ├── 🚗 Car Rental
│   ├── 💻 GitHub
│   ├── 🌐 Portfolio
│   └── ⬅ Back
│
└── 🤖 AI Features (Planned)
```

## 🔮 Future Improvements

* AI model Integration
* AI Chat Assistant
* Portfolio Website Integration
* Contact Section
* Skills & Experience Section
* Admin Dashboard
* Analytics Tracking

## 👨‍💻 Author

**Bahodirov Javohir**

* GitHub: https://github.com/Jovohir009
* Telegram Bot: @Artificial_SupportBot
* Number: 90 009 38 31

First-year Information Technology student passionate about software development, AI, automation, and building real-world digital products.
