import React from "react";
import Resume from "./Resume";
import { ResumeModel } from "./ResumeModel";
import {logOut} from "../auth/AuthService";
import {RouteComponentProps, withRouter} from "react-router";

class ResumeContainer extends React.Component<Props, State> {
  state = {
    resume: undefined,
  };

  render() {
    let resume: any = this.state.resume;
    return (
      <div>
        <div>
          <button onClick={this.logOut.bind(this)}>Fcuk it, I'm out!</button>
        </div>
        {resume ? <Resume basics={resume.basics} work={resume.work} /> : null}
      </div>
    );
  }

  componentDidMount() {
    this.getResumeFromServer();
  }

  private logOut() {
    logOut();
    this.props.history.push("/login");
  }

  private getResumeFromServer(): void {
    fetch("/api/resume")
      .then((response) => response.json())
      .then((value) => this.setState({ resume: value }));
  }
}

interface Props extends RouteComponentProps {}

interface State {
  resume?: ResumeModel;
}

export default withRouter(ResumeContainer);
