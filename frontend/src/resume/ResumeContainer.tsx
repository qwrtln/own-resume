import React from "react";
import Resume from "./Resume";
import { ResumeModel } from "./ResumeModel";

class ResumeContainer extends React.Component<Props, State> {
  state = {
    resume: undefined,
  };

  render() {
    let resume: any = this.state.resume;
    return (
      <div>
        {resume ? <Resume basics={resume.basics} work={resume.work} /> : null}
      </div>
    );
  }

  componentDidMount() {
    this.getResumeFromServer();
  }

  private getResumeFromServer(): void {
    fetch("/api/resume")
      .then((response) => response.json())
      .then((value) => this.setState({ resume: value }));
  }
}

interface Props {}

interface State {
  resume?: ResumeModel;
}

export default ResumeContainer;
