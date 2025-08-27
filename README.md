# Microservices-based-Todo-App
Todo management application built with a modern microservices architecture. It allows users to add, view, and manage their tasks using a responsive React frontend, a lightweight Flask backend API, and a Postgres database for persistent storage. To boost performance, it integrates Redis caching so frequently accessed task lists can be retrieved quickly without hitting the database every time.

This project is designed to demonstrate end-to-end containerized development with multiple services working together, covering:

Frontend (React) → clean UI for users.

Backend (Flask) → REST API handling requests.

Database (Postgres) → stores tasks persistently.

Cache (Redis) → improves read performance.

It’s a perfect learning project for practicing Docker, Docker Compose, service dependencies, networks, volumes, environment variables, and multi-stage builds—all within a real-world scenario.
