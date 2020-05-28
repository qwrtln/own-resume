import React from "react";
import {BasicsModel} from "./ResumeModel";
import photo from "../assets/photo.jpg"

const Basics: React.FC<BasicsModel> = (props) => (
  <React.Fragment>
    <div className="basics__name-section">
      <h1>{props.name}</h1>
      <h2>{props.summary}</h2>
    </div>
    <div className="basics__contact-section">
      <div>
        <span className="basics__contact-field-label">Mail:</span>
        <span>{props.email}</span>
      </div>
      <div>
        <span className="basics__contact-field-label">Phone:</span>
        <span>{props.email}</span>
      </div>
      <div>
        <span className="basics__contact-field-label">Website:</span>
        <span>{props.website}</span>
      </div>
    </div>
    <div className="basics__contact-section">
    </div>
    <div className="basics__side-section">
      <img src={photo} className="basics-photo"/>
      <h3>About me</h3>
    </div>
  </React.Fragment>
);

export default Basics;
