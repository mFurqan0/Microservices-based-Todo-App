# Microservices-based-Todo-App
Todo management application built with a modern microservices architecture. It allows users to add, view, and manage their tasks using a responsive React frontend, a lightweight Flask backend API, and a Postgres database for persistent storage. To boost performance, it integrates Redis caching so frequently accessed task lists can be retrieved quickly without hitting the database every time.

# Todo App (React + Flask + Postgres + Redis)

## Backend
- Flask API
- Postgres for persistent storage
- Redis for caching

## Frontend
- React simple UI

## Setup
1. Start Postgres and run `db_init.sql`.
2. Start Redis.
3. Run Flask backend:
