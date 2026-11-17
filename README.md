#  Dockerized Python Flask & SQLite To-Do List App

A lightweight, containerized full-stack To-Do List web application built with **Python (Flask)**, **SQLite**, **HTML5**, and **CSS3**. This project demonstrates how to package a web application with a relational database and ensure data persistence using **Docker Named Volumes**.



##  Features
* **Task Management:** Add new tasks and delete completed tasks seamlessly.
* **Persistent SQL Storage:** Uses SQLite with raw SQL queries (`CREATE TABLE`, `INSERT`, `SELECT`, `DELETE`) backed by a Docker Named Volume (`todo-data`) so tasks survive container restarts and removals.
* **Clean & Responsive UI:** Styled with modern CSS3 for a clean user experience.
* **Containerized Deployment:** Packaged into a lightweight `python:3.11-slim` Docker image for consistent execution across environments.



## Tech Stack
* **Backend:** Python 3.11, Flask
* **Database:** SQLite3
* **Frontend:** HTML5, CSS3 (Jinja2 Templating)
* **Containerization:** Docker, Docker Volumes

---

##  Project Structure

docker-todo-sql-app/
│
├── app.py              # Main Flask application & SQLite database logic
├── requirements.txt    # Python dependencies (Flask)
├── Dockerfile          # Instructions to build the Docker image
├── README.md           # Project documentation
├── templates/
│   └── index.html      # Frontend HTML template
└── static/
    └── style.css       # Application styling
How to Build & Run with Docker
1. Clone the Repository
git clone [https://github.com/hitakshi2021/docker-todo-sql-app.git](https://github.com/hitakshi2021/docker-todo-sql-app.git)
cd docker-todo-sql-app

2. Build the Docker Image
docker build -t todo-sql-app:v1 .

3. Create a Persistent Docker Volume
docker volume create todo-data

4. Run the Container
docker run -d --name my-todo-container -p 5000:5000 -v todo-data:/app todo-sql-app:v1

5.Access the Application
http://localhost:5000

Cleanup Commands
docker stop my-todo-container
docker rm my-todo-container
