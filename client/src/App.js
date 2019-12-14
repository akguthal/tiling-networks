import React, { useState, useEffect } from 'react'
import axios from 'axios'

import CommunityNode from './components/CommunityNode'
import './css/App.css'
import MemberNode from './components/MemberNode'

function App() {

    const [displayedNodes, setDisplayedNodes] = useState([])
    const [parent, setParent] = useState(-1)

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

    useEffect(() => {
        // code to run on component mount
        axios.get("http://localhost:5000/communities?parent=-1")
            .then(resp => {
                let nodes = resp.data.map(d => <CommunityNode id={d.cid} data={d} displayNodes={showNodes} />)
                setDisplayedNodes(nodes)
            })
      }, [])
    
    return (
     <div className="App">
        <h1>
            Tiling Networks
        </h1>
        <p class="description">This application is a novel way to explore large networks. Each blue node represents a community of members, and each white node represents an individual member. For community nodes, the count shows how many members are in that community.</p>
        <div className="communityNodesList">{displayedNodes}</div>
        { parent > -1 && <button className="backButton" onClick={goUpALevel}>Go Up</button> }
    </div>
    )
}

export default App
