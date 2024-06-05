import React, { useState } from 'react'
import TodoItem from './TodoItem';

const TodoList = () => {

    const [todos, setTodos] = useState([]);
    const [input, setInput] = useState('')

    const addTodo = () => {
        if (input) {
            const newTodo = {
                id: Date.now(),
                title: input,
                completed: false
            };
            setTodos([...todos, newTodo]);
            setInput('');
        }
    }

    const toggleTodo = (id) => {
        setTodos(
            todos.map(todo =>
                todo.id === id ? {...todo, completed: !todo.completed} : todo
            )
        )
    }

    return (
        <>
            <h2>Todo List</h2>
            <input type="text" placeholder='Add a task' value={input} onChange={e => setInput(e.target.value)} />
            <button onClick={addTodo}>Add Todo</button>

            <div>
                {
                    todos.map(todo => (
                        <TodoItem key={todo.id} todo={todo} toggleTodo={ toggleTodo } />
                    ))
                }
            </div>
        </>
    )
}

export default TodoList;