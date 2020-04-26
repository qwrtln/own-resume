import React from "react";
import "./Resume.css";
import { ResumeModel } from "./ResumeModel";
import Basics from "./Basics";
import Workplaces from "./Workplaces";

const Resume: React.FC<ResumeModel> = (props) => (
  <div>
    <Basics {...props.basics} />
    {shouldRenderWorkplacesSection(props) && (
      <Workplaces workplaces={props.work} />
    )}
  </div>
);

const shouldRenderWorkplacesSection = (props: ResumeModel) => {
  return props.work.length > 0;
};

export default Resume;
