import React from 'react';
import "./Resume.css"
import {ResumeModel} from "./ResumeModel";
import Basics from "./Basics";
import Workplaces from "./Workplaces";

const Resume: React.FC<ResumeModel> = (props) => (
    <div>
        <Basics {...props.basics}/>
        <Workplaces workplaces={props.work}/>
    </div>
);

export default Resume;
