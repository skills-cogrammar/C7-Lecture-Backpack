import './App.css';
import useNotes from './hooks/useNotes';
import useLocalStorage from './hooks/useLocalStorage';

function App() {
  const [storedNotes, setStoredNotes] = useLocalStorage('notes', [])
  const { notes, addNote, editNote, deleteNote } = useNotes(storedNotes)

  return (
    <div className="App">
      <h1>Notes</h1>
      <form onSubmit={
        (event) => {
          event.preventDefault();
          const note = event.target.elements.note.value
          addNote({
            id: Date.now(),
            content: note
          });
          event.target.reset();
        }
      }>
        <input type="text" name="note" placeholder='Enter a note!' />
        <button type='submit'>Add Note</button>
      </form>
      <ul>
        {
          notes.map((note) => (
            <li key={note.id}>
              {note.content}
              <button onClick={() => {
                const newContent = prompt('Enter new content', note.content)
                if (newContent) {
                  editNote(note.id, newContent)
                }
              }} >Edit</button>
              <button onClick={() => deleteNote(note.id)}>Delete</button>
            </li>
          ))
        }
        
      </ul>
      <button onClick={() => {
        const confirmation = window.confirm("Clear all note?")
        if (confirmation) {
          setStoredNotes([])
        }
      }}>Clear All Notes</button>
    </div>
  );
}

export default App;
