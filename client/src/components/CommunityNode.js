import React, { useState } from 'react'
import axios from 'axios'

import MemberNode from './MemberNode'
import '../css/components/CommunityNode.css';

function CommunityNode(props) {

    const [nodes, setNodes] = useState([])
    const [members, setMembers] = useState([])
    const [expanded, setExpanded] = useState(false)
    const [loadedIntoMemory, setLoadedIntoMemory] = useState(false)


    const data = props.data

    const handleClick = () => {
        if (expanded) {
            collapse()
        }
        else {
            expand()
        }
    }

    const expand = () => {
        setExpanded(true)
        if (data.leaf && !loadedIntoMemory) {
            axios.get("http://localhost:5000/members?community="+data.cid)
                .then(resp => {
                    setNodes([])
                    setMembers(resp.data)
                    setLoadedIntoMemory(true)
                })
        }
        else if (!loadedIntoMemory) {
            axios.get("http://localhost:5000/communities?parent="+data.cid)
            .then(resp => {
                setNodes(resp.data)
                setMembers([])
                setLoadedIntoMemory(true)
            })
        }
    }

    const collapse = () => {
        setExpanded(false)
    }

    let renderedNodes = []
    let renderedMembers = []

    let classnames = "communityNode"
    if (expanded) {
        renderedNodes = nodes.map( (nodeData) => <CommunityNode id={nodeData.cid} data={nodeData} /> )
        renderedMembers = members.map( (memberData) => <MemberNode data={memberData} /> )
        classnames += " communityNode_expanded"    
    }

    return (
        <div className="communityNodes_column">
            <div className={classnames} onClick={handleClick}>
                <p className="communityNode_name">{data.cid}</p>
                <p className="communityNode_count">Sum: {data.sum}</p>
            </div>
            { renderedMembers }
            { renderedNodes }
        </div>
  );
}

export default CommunityNode;
