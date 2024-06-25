import { useState } from "react";

function useNotes(initialNotes) {
    const [notes, setNotes] = useState(initialNotes);

    const addNote = (note) => {
        setNotes([...notes, note]) // adding a new note
    }

    const editNote = (id, newContent) => {
        setNotes(notes.map(note => note.id === id ? { ...note, content: newContent } : note));
    }

    const deleteNote = (id) => {
        setNotes(notes.filter(note => note.id !== id)) // removes the note with the specified ID
    }

    return { notes, addNote, editNote, deleteNote }
}

export default useNotes;