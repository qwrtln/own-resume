import React from "react";
import Resume from "./Resume";
import {ResumeModel} from "./ResumeModel";

class ResumeContainer extends React.Component<Props, State> {
  state = {
    resume: undefined
  };

  render() {
    return (
      <div>
        {this.renderResume()}
      </div>
    );
  }

  private renderResume() {
    let resume: any = this.state.resume;
    return resume ? <Resume basics={resume.basics} work={resume.work}/> : null;
  }

  componentDidMount() {
    this.getResumeFromRedux();
  }

  private getResumeFromRedux(): void {
    fetch('/api/resume')
      .then(response => response.json())
      .then(value => {
        console.log(value);
        this.setState({resume: value});
      })
  }
}

interface Props {
}

interface State {
  resume?: ResumeModel
}

export default ResumeContainer;
