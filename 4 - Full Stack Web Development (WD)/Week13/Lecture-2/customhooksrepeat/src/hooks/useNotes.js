import { useState } from "react";

//Function declaration
const useNotes = (initialNotes) => { //Function parameters (What the function expects)
  //Function definition
  const [notes, setNotes] = useState(initialNotes); //notes = []

  const addNote = (note) => {
    setNotes([...notes, note]);
  };

  const editNote = (id, newContent) => {
    setNotes(
      notes.map((note) =>
        note.id === id ? { ...note, content: newContent } : note
      )
    );
  };

  const deleteNote = (id) => {
    setNotes(notes.filter((note) => note.id !== id));
  };

  return {
    notes,
    addNote,
    editNote,
    deleteNote
  }
};

export default useNotes;

