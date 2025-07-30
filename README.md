# EcoHub

**EcoHub** is a Django-powered web platform for sharing, discovering, and discussing eco-friendly articles, tips, and sustainable living practices. It’s designed to foster a community of environmentally conscious users, providing tools to learn, contribute, and track their own sustainability journey.

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About

EcoHub is your comprehensive guide to sustainable living. The platform enables users to:
- Share and discover articles on renewable energy, green technology, and eco-friendly lifestyles.
- Post practical tips for reducing environmental impact.
- Engage with a community through comments and favorites.
- Track their own eco-journey and history.

---

## Features

- **User Authentication**: Register, log in, log out, reset password, and manage user profiles.
- **Articles**: Create, read, update, and delete articles with categories and images.
- **Tips**: Share eco-friendly tips, including file uploads.
- **Comments**: Comment on articles to foster discussion.
- **Favorites**: Save favorite articles for quick access.
- **Search**: Powerful search with category filtering for articles and tips.
- **User History**: Track your visits and activity.
- **Responsive UI**: Modern, green-themed Bootstrap interface.
- **Admin Panel**: Manage users, articles, tips, and more.

---

## Screenshots

> _You can add screenshots here to showcase the UI and features._

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Harsh3827/Ecohub
   cd Project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **(Optional) Load sample data**
   ```bash
   python manage.py loaddata sample_data.json
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

---

## Project Structure

```
Project/
├── accounts/      # User authentication and profiles
├── articles/      # Articles, comments, favorites
├── tips/          # Eco-friendly tips and uploads
├── core/          # Home, about, contact, search, user history
├── templates/     # HTML templates
├── static/        # Static files (CSS, JS, images)
├── media/         # User uploads
├── ecohub/        # Main project settings
├── requirements.txt
└── manage.py
```

---

## Usage

- **Browse**: Anyone can browse articles and tips.
- **Register/Login**: Create an account to contribute content and interact.
- **Post Articles/Tips**: Share your knowledge and eco-friendly practices.
- **Comment & Favorite**: Engage with the community.
- **Track History**: See your own activity and contributions.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## License

This project is for educational use only as part of the COMP-8347 Internet Applications and Distributed Systems course at the University of Windsor.

---
