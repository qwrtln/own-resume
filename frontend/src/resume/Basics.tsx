import React from 'react';
import {BasicsModel} from "./ResumeModel";

const Basics: React.FC<BasicsModel> = (props) => (
    <div>
        <div className="resume-basics-section">
            <div><h2>Name:</h2></div>
            <div><h2>{props.name}</h2></div>

            <div><h2>Mail:</h2></div>
            <div><h2>{props.email}</h2></div>
        </div>
    </div>
);

export default Basics;
