import { useEffect, useState } from "react";
import useNotes from "./hooks/useNotes";
import useLocalStorage from "./hooks/useLocalStorage";
import Random from "./Random";

function App() {
  const [ value, setValue ] = useState("")
  const { value:localStorageValue, setValue:setLocalStorage } = useLocalStorage("notes", [])
  const { notes, addNote, editNote, deleteNote } = useNotes(localStorageValue);
  

  const handleSubmit = (e)=>{
    e.preventDefault()
    addNote({
      id: notes.length + 1,
      content: value
    })
  }




  const handleEdit = (id)=>{
    const submitContent = prompt("Enter a content")
    editNote(id, submitContent)
  }

  useEffect(()=>{
    setLocalStorage(notes)
  }, [notes])


  return (
    <div className="flex w-full flex-col gap-4">
    <form className="flex flex-col" onSubmit={handleSubmit}>
      <input name="Note" placeholder="Enter a note" value={value} onChange={(e)=>setValue(e.target.value)}/>
      <button className="bg-green-500 p-2">Submit</button>
    </form>
      {notes.map((note) => {
        return (
          <div key={note.id} className="flex gap-4">
            <p>{note.content}</p>
            <div className="flex gap-2">
              <button className="bg-orange-500 p-2 rounded-lg" onClick={(e)=>handleEdit(note.id)}>Update</button>
              <button className="bg-red-600 p-2 rounded-lg" onClick={()=>deleteNote(note.id)}>Delete</button>
            </div>
          </div>
        );
      })}
      <Random/>
    </div>
  );
}

export default App;
