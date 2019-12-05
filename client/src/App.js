import React, { useState, useEffect } from 'react'
import axios from 'axios'

import CommunityNode from './components/CommunityNode'
import './css/App.css'

function App() {

    const [root, setRoot] = useState(null)

    useEffect(() => {
        // code to run on component mount
        axios.get("http://localhost:5000/communities?parent=-1")
            .then(resp => {
                setRoot(resp.data[0])
            })
      }, [])
    
    return (
     <div className="App">
        <h1>
            Tiling Networks
        </h1>
        { root === null ? '' : <div className="communityNodesList"><CommunityNode id={root.cid} data={root} /></div> }
    </div>
    )
}

export default App
