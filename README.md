# 📝 Django Blog - Personal Blog with Django

<p align="center">
  <img src="https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status"/>
</p>

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2MzeGg0eGlweTlxZzN6a3Z4ejR4eXN1YzFqZmg5dGJ5amYwdmFkMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/coxQHKASG60HrHtvkt/giphy.gif" width="400" alt="Coding"/>
</p>

---

## 📖 About The Project

This is a **fully dynamic blog** built with **Django** and **HTML & CSS**.  
The goal was to implement a simple yet professional Content Management System (CMS) with the following features:

- 📝 **Create, edit, and manage posts** (admin panel)
- 🗂 **Category-based organization**
- 💬 **Comment system** (user submission + admin approval)
- 👤 **Author profile**
- 📬 **Contact form**
- 🔍 **Advanced search & filtering** (admin panel)
- 🎨 **Responsive & user-friendly design**

This project is the result of my deep learning in **Django, HTML, CSS**, and full-stack web development concepts.

---

## ✨ Features

| Section | Description |
|:---|:---|
| **Admin Panel** | Full control over posts, categories, comments, users, and messages |
| **Posts** | CRUD operations with author, date, and category |
| **Categories** | Topic-based grouping |
| **Comments** | User-submitted, admin-approved |
| **Profile** | Author bio page |
| **Contact** | Visitor contact form |
| **Search** | Advanced filtering in admin panel |

---

## 🛠️ Tech Stack

- **Back-End:** Python 3.x, Django 4.x
- **Front-End:** HTML5, CSS3
- **Database:** SQLite (Django default)
- **Static Files:** Django Static Files Management
- **Version Control:** Git & GitHub

---

## 🚀 Installation & Setup

### 📋 Prerequisites

| Tool | Version |
|:---|:---|
| Python | 3.8 or higher |
| pip | Latest |
| Git | (optional - for cloning) |

### ⚙️ Setup Steps

```bash
# 1. Clone the repository
git clone https://github.com/seyedAlirezahn1/django-blog.git
cd django-blog

# 2. Create a virtual environment (recommended)
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations (create database tables)
python manage.py migrate

# 6. Create superuser (admin)
python manage.py createsuperuser
# Enter username, email, and password

# 7. Run development server
python manage.py runserver

```
---
##🎉 Now open your browser:

Blog: http://127.0.0.1:8000

Admin Panel: http://127.0.0.1:8000/admin
