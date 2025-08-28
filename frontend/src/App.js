import React, { useState, useEffect } from "react";
import axios from "axios";
import TodoList from "./components/TodoList";

function App() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState("");

  useEffect(() => {
    axios.get("http://localhost:5000/tasks")
      .then(res => setTasks(res.data.tasks))
      .catch(err => console.error(err));
  }, []);

  const addTask = () => {
    axios.post("http://localhost:5000/tasks", { task: newTask })
      .then(res => {
        setTasks([...tasks, res.data]);
        setNewTask("");
      })
      .catch(err => console.error(err));
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Todo App</h2>
      <input
        value={newTask}
        onChange={e => setNewTask(e.target.value)}
        placeholder="Add task..."
      />
      <button onClick={addTask}>Add</button>
      <TodoList tasks={tasks} />
    </div>
  );
}

export default App;
