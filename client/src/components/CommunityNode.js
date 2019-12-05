import React from 'react';
import '../css/components/CommunityNode.css';

function CommunityNode(props) {

    const expandFunc = props.expandFunc
    const data = props.data

    function handleClick(e) {
        expandFunc(data.cid)
    }

    return (
        <div className="communityNode" onClick={handleClick}>
            <p className="communityNode_name">{data.cid}</p>
            <p className="communityNode_count">Sum: {data.sum}</p>
        </div>
  );
}

export default CommunityNode;
