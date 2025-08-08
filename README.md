# 🎬 Movie API Project

A Django project that provides a **RESTful API** for managing movie data. The API allows you to create, view, filter, and manage movie entries, including details like **name**, **duration**, **rating**, and **genre**. It also supports **image uploads** for each movie.

---

## ✨ Features

* 🎥 **Movie Data Management** – Create, retrieve, update, and delete movie entries
* 🔍 **Filtering** – Filter movies by type (e.g., `action`, `adventure`)
* 🖼 **Image Uploads** – Associate an image with each movie entry

---

## 🛠 Tech Stack

* **Backend Framework:** Django
* **API Framework:** Django REST Framework
* **Database:** SQLite3

---

## 📡 API Endpoints

| Endpoint      | Method | Description                            |
| ------------- | ------ | -------------------------------------- |
| `/movies/`    | GET    | Lists all movies                       |
| `/action/`    | GET    | Lists all movies with type `action`    |
| `/adventure/` | GET    | Lists all movies with type `adventure` |
| `/admin/`     | GET    | Django admin interface                 |

---

## 🗄 Database Schema

The primary model **`MovieData`** (defined in `movies/models.py`) contains:

| Field      | Type                             | Description                                             |
| ---------- | -------------------------------- | ------------------------------------------------------- |
| `id`       | BigAutoField                     | Primary key                                             |
| `name`     | CharField(200)                   | Movie name                                              |
| `duration` | FloatField                       | Duration of the movie                                   |
| `rating`   | FloatField                       | Movie rating                                            |
| `typ`      | CharField(200, default='action') | Movie type/genre                                        |
| `image`    | ImageField                       | Uploads to `Images/` (default: `Images/None/Noimg.jpg`) |

---

## 🚀 Setup & Installation

### 1️⃣ Prerequisites

* Python 3.x
* Django & Django REST Framework installed

```bash
pip install django djangorestframework pillow
```

### 2️⃣ Clone the Repository

```bash
git clone <repository-url>
cd movie-api-project
```

### 3️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 4️⃣ Run the Development Server

```bash
python manage.py runserver
```

### 5️⃣ Access the API

* API root: [http://127.0.0.1:8000/movies/](http://127.0.0.1:8000/movies/)
* Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

If you want, I can also **add example API requests with sample JSON data** so people can test your endpoints quickly. That will make your README much more developer-friendly.
