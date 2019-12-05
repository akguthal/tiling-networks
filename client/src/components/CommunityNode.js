import React from 'react'
import axios from 'axios'

import '../css/components/CommunityNode.css';

function CommunityNode(props) {

    const data = props.data
    const displayNodes = props.displayNodes // function from parent component to expand the node

    const handleClick = () => {
        expand()
    }

    const expand = () => {
        // setExpanded(true)
        if (data.leaf) {
            axios.get("http://localhost:5000/members?community="+data.cid)
                .then(resp => {
                    displayNodes(resp.data, data.cid, true)
                })
        }
        else {
            axios.get("http://localhost:5000/communities?parent="+data.cid)
            .then(resp => {
                displayNodes(resp.data, data.cid, false)
            })
        }
    }

    return (
        <div className="communityNode" onClick={handleClick}>
            <p className="communityNode_name">{data.cid}</p>
            <p className="communityNode_count">Sum: {data.sum}</p>
        </div>
  );
}

export default CommunityNode;
