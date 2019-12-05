import React, { useState, useEffect } from 'react'
import axios from 'axios'

import CommunityNode from './components/CommunityNode'
import './css/App.css'
import MemberNode from './components/MemberNode'

function App() {

    const [displayedNodes, setDisplayedNodes] = useState([])
    const [parent, setParent] = useState(-1)

    useEffect(() => {
        // code to run on component mount
        axios.get("http://localhost:5000/communities?parent=-1")
            .then(resp => {
                let data = resp.data[0]
                let root = <CommunityNode id={data.cid} data={data} displayNodes={showNodes} />
                setDisplayedNodes([root])
            })
      }, [])

    const showNodes = (nodeDataList, parentId, showMembers) => {
        let renderedNodes = []
        if (showMembers) {
            renderedNodes = nodeDataList.map( (nodeData) => <MemberNode data={nodeData} /> )
        }
        else {
            renderedNodes = nodeDataList.map( (nodeData) => <CommunityNode id={nodeData.cid} data={nodeData} displayNodes={showNodes} /> )
        }
        setParent(parentId)
        setDisplayedNodes(renderedNodes)
    }

    const goUpALevel = () => { // gets the grandparent's children (one level up)
        axios.get("http://localhost:5000/communities/"+parent)
        .then(resp => {
            let grandparent = resp.data.parent
            axios.get("http://localhost:5000/communities?parent="+grandparent)
            .then(resp2 => {
                showNodes(resp2.data, grandparent)
            })            
        })
    }
    
    return (
     <div className="App">
        <h1>
            Tiling Networks
        </h1>
        <div className="communityNodesList">{displayedNodes}</div>
        { parent > -1 && <button className="backButton" onClick={goUpALevel}>Go Up</button> }
    </div>
    )
}

export default App
