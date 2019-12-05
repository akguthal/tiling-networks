import React, { useState, useEffect } from 'react'
import axios from 'axios'
import CommunityNode from './components/CommunityNode'
import './css/App.css'

function App() {

    const [nodes, setNodes] = useState([])

    const expand = (id) => {
        // dummy code to update list with children
        axios.get("http://localhost:5000/communities?parent="+id)
            .then(resp => {
                setNodes(resp.data)
            })
        // let dummyNodes = [...Array(nodes.length*2).keys()]
        // dummyNodes = dummyNodes.map( (num) => "node"+num )
        // setNodes(dummyNodes)
    }

    useEffect(() => {
        // code to run on component mount
        axios.get("http://localhost:5000/communities?parent=-1")
            .then(resp => {
                setNodes(resp.data)
            })
      }, [])

    
    let renderedNodes = nodes.map( (nodeData) => <CommunityNode id={nodeData.cid} data={nodeData} expandFunc={expand} /> )
 
    return (
     <div className="App">
        <h1>
            Tiling Networks
        </h1>
        <div className = "communityNodesList">
            { renderedNodes }
        </div>
    </div>
    )
}

export default App
