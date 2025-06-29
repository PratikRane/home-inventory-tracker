# 🏠 Home Inventory Tracker

A simple web-based inventory app to track household items and avoid duplicate purchases. Built with Flask + MySQL, and fully containerized using Docker Compose.

---

## 📦 Features

- Add items with purchase date and position
- Optional spatial relationship (inside, above, below, left, right)
- Support for consumable items and expiry dates
- Dockerized setup with secrets in `.env` file

---

## 🛠 Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 🚀 Quick Start

```bash
git clone https://github.com/yourusername/home-inventory-tracker.git
cd home-inventory-tracker
cp secrets.env.example secrets.env   # Create your env file
nano secrets.env                     # Edit credentials
docker-compose up --build



---

### ✅ Step-by-Step Setup Summary

1. Install Docker and Docker Compose.
2. Clone the repo.
3. Run: `docker-compose up --build`
4. Visit `http://localhost:5000` in your browser.

---

Would you like me to zip and share the full structure as a downloadable file or help push this to GitHub?
