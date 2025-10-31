
# 🍽️ Django FoodApp

A simple CRUD-based web application built using the **Django Framework**, where users can **add, update, view, and delete food items** with authentication and profile integration.

---

## 🧰 Tech Stack

* **Backend:** Django (Python 3.12+)
* **Frontend:** HTML, CSS, Bootstrap 4
* **Database:** SQLite (default Django DB)
* **Environment:** Conda / Virtualenv
* **Libraries:** Pillow (for image handling)

---

## ⚙️ Setup Instructions

### 1️⃣ Create a Virtual Environment

```bash
conda create --name myDjangoEnv python=3.12.0
conda activate myDjangoEnv
pip install django pillow
```

### 2️⃣ Create a Django Project and App

```bash
django-admin startproject food_project
cd food_project
python manage.py startapp food_app
```

### 3️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 5️⃣ Run the Server

```bash
python manage.py runserver
```

Visit 👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📂 Project Structure

```
food_project/
│
├── food_app/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/food/
│       ├── base.html
│       ├── index.html
│       ├── detail.html
│       ├── item-form.html
│       └── item-delete.html
│
├── users/
│   ├── views.py
│   └── templates/users/
│       ├── login.html
│       ├── logout.html
│       └── profile.html
│
├── static/
│   └── food/style.css
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## 🧩 Key Features

✅ **User Authentication**

* Register, login, logout using Django’s built-in user model.
* Profile page for each user.

✅ **CRUD Operations**

* Add new food items.
* View all food items with details.
* Update or delete existing items.

✅ **Class-Based and Function-Based Views**

* Uses Django’s `ListView`, `DetailView`, and `CreateView` for modular design.

✅ **Dynamic Templates**

* Responsive frontend with Bootstrap.
* Template inheritance via `base.html`.

✅ **Admin Panel**

* Manage all food items and users via Django Admin.

---

## 💾 Example Model

```python
class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.item_name
```

---

## 🧮 URLs Overview

| Path                 | Description                    |
| -------------------- | ------------------------------ |
| `/food/`             | Home page (list of food items) |
| `/food/<id>/`        | Item detail view               |
| `/food/add`          | Add a new food item            |
| `/food/update/<id>/` | Update an item                 |
| `/food/delete/<id>/` | Delete an item                 |
| `/register/`         | User registration              |
| `/login/`            | User login                     |
| `/logout/`           | Logout                         |
| `/profile/`          | Profile page                   |

---

## 🧑‍💻 Example Usage in Shell

```python
from food_app.models import Item
Item.objects.create(item_name="Pizza", item_desc="Cheesy Pizza", item_price=20)
Item.objects.create(item_name="Burger", item_desc="Cheesy Burger", item_price=10)
Item.objects.create(item_name="Biryani", item_desc="Chicken Biryani", item_price=30)
```

---

## 📸 Screenshots

<img width="1373" height="824" alt="Food_App" src="https://github.com/user-attachments/assets/218cb237-03d4-4abf-a9ba-e4f00e9075b4" />

<img width="1912" height="798" alt="Food_menu" src="https://github.com/user-attachments/assets/d72c5308-b5c5-4e6f-b371-fb58d34bfb56" />

<img width="948" height="628" alt="Pizza" src="https://github.com/user-attachments/assets/b8f3e3a1-f90d-45f7-b1f2-16c57545a019" />

<img width="1048" height="638" alt="Add_food" src="https://github.com/user-attachments/assets/d292c123-8a86-4235-bd47-2f0f5a9d0d98" />


---

## 🧠 Future Enhancements

* Add image upload support using `ImageField`.
* Implement search and filtering.
* Include pagination.
* Add API endpoints using Django REST Framework.

---
