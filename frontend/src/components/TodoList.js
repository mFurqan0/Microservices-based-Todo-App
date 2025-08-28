import React from "react";

function TodoList({ tasks }) {
  return (
    <ul>
      {tasks.map(t => (
        <li key={t.id}>{t.task}</li>
      ))}
    </ul>
  );
}

export default TodoList;
