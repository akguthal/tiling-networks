import React from 'react';
import '../css/components/MemberNode.css';

function MemberNode(props) {

    const data = props.data

    return (
        <div className="memberNode">
            <p className="memberNode_name">{data.member}</p>
            {/* <p className="memberNode_value">Value: {data.value}</p> */}
        </div>
  );
}

export default MemberNode;
