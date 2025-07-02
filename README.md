### ✅ Simple Django Blog (No Auth)

````markdown
# 📝 Simple Django Blog

A basic Django blog application that allows users to:
- Create blog posts with images and content
- Edit and delete posts
- View all posts on the homepage

🔒 No user authentication — for learning or personal project use.

---

## 🚀 Features

- Create blog posts with title, image, and content
- Edit existing posts
- Delete posts
- Upload and display images
- Simple and clean interface

---

## 📦 Requirements

- Python 3.x
- Django 4.x+
- Pillow (for image upload handling)

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/simple-django-blog.git
cd simple-django-blog
````

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # on Windows use `venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note**: If `requirements.txt` is missing, just run:
>
> ```bash
> pip install django pillow
> ```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 📁 Project Structure

```
blogger/
│
├── blog/               # Blog app (views, models, templates, etc.)
│   ├── migrations/
│   ├── templates/
│   └── static/
│
├── blogger/       # Django project settings
├── media/              # Uploaded images
├── db.sqlite3          # SQLite database
└── manage.py
|__ media
|   |__ blog_images
```

---

## 🧪 Future Improvements

* Add user authentication
* Add comments
* Add tags/categories

---

## 📄 License

MIT License. Feel free to use and modify for your own projects.

Let me know if you'd like this customized with:
- Your GitHub repo link
- Commands for creating the blog app
- Example models or views

I can also help you generate the actual Django app step-by-step if you're starting from scratch.
```
