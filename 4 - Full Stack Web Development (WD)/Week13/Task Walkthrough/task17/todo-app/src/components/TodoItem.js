import React from "react";

const TodoItem = ({todo, toggleTodo}) => {
    const { id, title, completed } = todo;

    return (
        <>
            <input type="checkbox" checked={completed} onChange={() => toggleTodo(id)} />
            <label>{ title }</label>
        </>
    )
}

export default TodoItem;