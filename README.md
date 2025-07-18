# EcoHub - Your Guide to Sustainable Living

A Django-based web application for sharing and discovering eco-friendly articles, tips, and sustainable living practices.

## 🌱 Project Overview

EcoHub is a comprehensive platform that promotes environmental awareness and sustainable living. Users can share articles about renewable energy, green technology, and eco-friendly practices, as well as practical tips for reducing their environmental impact.

## ✨ Features

### Core Features
- **User Authentication**: Registration, login, logout, password reset, and user profiles
- **Articles System**: Create, read, update, and delete articles with categories
- **Tips System**: Share eco-friendly tips with file upload support
- **Comments**: Users can comment on articles
- **Search Functionality**: Search articles and tips with category filtering
- **User History**: Track user visits and activity using sessions/cookies
- **Responsive Design**: Bootstrap-based UI with green theme

### User Roles
- **Unregistered Users**: Can browse articles and tips, search content
- **Registered Users**: Can create articles/tips, comment, upload files, view history

## 🛠️ Technology Stack

- **Backend**: Django 5.2.1
- **Database**: SQLite (development)
- **Frontend**: Bootstrap 5.1.3
- **Image Processing**: Pillow
- **Authentication**: Django's built-in auth system

## 📁 Project Structure

```
ecohub/
├── accounts/          # User authentication and profiles
├── articles/          # Articles, comments, favorites
├── tips/             # Eco-friendly tips and uploads
├── core/             # Home, about, contact, search, user history
├── templates/        # Base template and shared templates
├── static/           # Static files (CSS, JS, images)
├── media/            # User uploads
└── ecohub/           # Main project settings
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ecohub
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Load sample data (optional)**
   ```bash
   python manage.py loaddata sample_data.json
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 👥 Team Contributions

### Student 1 - Authentication & User Management
- User registration, login, logout functionality
- Password reset implementation
- User profile system with UserProfile model
- User history tracking using sessions/cookies
- Profile picture upload functionality

### Student 2 - Articles System & Search
- Article model with categories and image upload
- Class-based views for article CRUD operations
- Search functionality with dropdown filtering
- Article list and detail views
- Bootstrap integration and responsive design

### Student 3 - Tips System & File Uploads
- Tip model with file upload support
- Class-based views for tip CRUD operations
- File upload handling and storage
- Tip forms and validation
- Media file configuration

### Student 4 - Comments, UI/UX & Core Features
- Comment system for articles
- Favorites functionality
- Core app views (home, about, contact)
- User history page
- Footer design and navigation
- Overall UI/UX improvements

## 📋 Requirements Met

### Mandatory Features ✅
- [x] Django, Python, PyCharm usage
- [x] Green/environment-friendly theme
- [x] User registration, login, logout, forgot password
- [x] Different interfaces for registered/unregistered users
- [x] Search bar with dropdown filtering
- [x] User history tracking (sessions/cookies)
- [x] File upload functionality
- [x] Footer with contact information
- [x] Eye-catching design with Bootstrap
- [x] Multiple models, views, templates, forms

### Additional Features ✅
- [x] JSON fixtures for initial data
- [x] Class-based views for index and detail pages
- [x] Bootstrap styling throughout
- [x] Extra pages (about, contact, team details)
- [x] Admin interface configuration
- [x] Responsive design

## 🔧 Admin Access

- **Username**: admin
- **Password**: (set during superuser creation)
- **Admin URL**: http://127.0.0.1:8000/admin/

## 📱 Key URLs

- **Home**: http://127.0.0.1:8000/
- **Articles**: http://127.0.0.1:8000/articles/
- **Tips**: http://127.0.0.1:8000/tips/
- **Search**: http://127.0.0.1:8000/search/
- **About**: http://127.0.0.1:8000/about/
- **Contact**: http://127.0.0.1:8000/contact/
- **User History**: http://127.0.0.1:8000/history/ (login required)

## 🎨 Design Features

- **Green Color Scheme**: Environmentally themed colors
- **Bootstrap 5**: Modern, responsive design
- **Card-based Layout**: Clean presentation of content
- **Navigation**: Easy access to all features
- **Footer**: Contact information and quick links

## 🔒 Security Features

- CSRF protection
- User authentication and authorization
- File upload validation
- SQL injection protection (Django ORM)
- XSS protection (Django templates)

## 📊 Database Models

### UserProfile
- User (OneToOneField to User)
- Bio, profile picture, visit tracking

### Article
- Title, content, author, category, image, created_at

### Comment
- Article, user, content, created_at

### Favorite
- User, article, added_at

### Tip
- Title, description, user, category, file_upload, created_at

## 🚀 Deployment Notes

For production deployment:
1. Set `DEBUG = False` in settings.py
2. Configure a production database (PostgreSQL recommended)
3. Set up static file serving
4. Configure media file storage
5. Set up environment variables for sensitive data

## 📝 License

This project is created for educational purposes as part of the COMP-8347 Internet Applications and Distributed Systems course at the University of Windsor.

---

**EcoHub Team** - University of Windsor, 2025 #
