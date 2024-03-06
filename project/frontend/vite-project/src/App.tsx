import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [result, setResult] = useState<string>('');

  const fetchData = async () => {
    try {
      const res = await fetch("http://127.0.0.1:5000/", {
        method: "GET",
        headers: {
          "Content-Type": "application/json"
        }
      });

      if (res.ok) {
        const data = await res.json();
        console.log(data);
        setResult(data);
      } else {
        setResult('Request failed with status: ' + res.status);
      }
    } catch (error) {
      setResult('An error occurred: ' + (error as Error).message);
    }
  };


  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>ça marche</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          here is the count : {count}
        </button>
        <p>
          Api call : {result} !
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
