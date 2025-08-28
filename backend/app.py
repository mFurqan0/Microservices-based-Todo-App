from flask import Flask, request, jsonify
import psycopg2
import redis
import os

app = Flask(__name__)

# Postgres connection
DB_HOST = os.getenv("DB_HOST", "db")  # 👈 default to docker service name
DB_NAME = os.getenv("DB_NAME", "todo_db")
DB_USER = os.getenv("DB_USER", "user")
DB_PASS = os.getenv("DB_PASS", "password")

# Redis connection
REDIS_HOST = os.getenv("REDIS_HOST", "redis")  # 👈 default to redis service
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    cached_tasks = r.get("tasks")
    if cached_tasks:
        return jsonify({"source": "cache", "tasks": eval(cached_tasks)})

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, task FROM tasks;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    tasks = [{"id": row[0], "task": row[1]} for row in rows]
    r.set("tasks", str(tasks))  # cache results
    return jsonify({"source": "db", "tasks": tasks})

@app.route("/tasks", methods=["POST"])
def add_task():
    task = request.json.get("task")
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (task) VALUES (%s) RETURNING id;", (task,))
    task_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    r.delete("tasks")  # clear cache
    return jsonify({"id": task_id, "task": task}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
