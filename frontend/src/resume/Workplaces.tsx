import React from "react";
import { WorkModel } from "./ResumeModel";

const Workplaces: React.FC<WorkplacesModel> = (props) => (
  <div className="workplaces">
    <h2>Workplaces:</h2>
    {props.workplaces.map((workplace) => (
      <div key={workplace.company} className="workplace">
        <h3>{workplace.company}</h3>
        <h4>{workplace.position}</h4>
        <div>
          <div>
            <h5>Summary: {workplace.summary}</h5>
          </div>
        </div>
      </div>
    ))}
  </div>
);

interface WorkplacesModel {
  workplaces: WorkModel[];
}

export default Workplaces;
