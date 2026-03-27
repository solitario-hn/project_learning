
import { useState } from 'react'
function App() {

  const [email , setemail] = useState("")
  const [password,pass]=useState(" ")


  async function callingbackend() {
     try {
      const response = await fetch('http://127.0.0.1:8000/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        // body: JSON.stringify(postData),
      });
      console.log(response)
    } catch (err) {
      console.error('There was an error!', err);
    }
  }

  return (
<div className='bg-black h-screen w-full text-white'>
<div className='text-[12px] bg-red flex flex-col'>
  <h1>SIgnup</h1>
 <h1>Email</h1>
 <input className='bg-white' type="text" onChange={(e) => {setemail(e.target.value)}} />
 <h1>Password</h1>
 <input  className='bg-white' type="text" onChange={(e) => {pass(e.target.value)}} />
 <button className='bg-white border-red-500 text-black' onClick={callingbackend}>Submit</button>
</div> 
</div>

  )
}

export default App
