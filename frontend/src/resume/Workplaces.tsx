import React from 'react';
import { WorkModel} from "./ResumeModel";

const Workplaces: React.FC<WorkplacesModel> = (props) => (
    <div>
        <h2>Workplaces:</h2>
        {props.workplaces.map(workplace => (
            <React.Fragment>
                <h3>{workplace.company}</h3>
                <h4>{workplace.position}</h4>
                <div className="resume-workplace-section">
                    <div><h5>Summary: {workplace.summary}</h5></div>
                </div>
            </React.Fragment>
        ))}

    </div>
);

interface WorkplacesModel {
    workplaces: WorkModel[]
}

export default Workplaces;
