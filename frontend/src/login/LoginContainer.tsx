import React from "react";
import { RouteComponentProps, withRouter } from "react-router";

import { logIn } from "../auth/AuthService";

class ResumeContainer extends React.Component<Props, State> {
  render() {
    return (
      <div>
        <h2>Who are you, Visitor?</h2>
        <button onClick={this.authenticate.bind(this)}>
          Login
        </button>
      </div>
    );
  }

  private authenticate() {
    logIn();
    this.props.history.push("/");
  }
}

interface Props extends RouteComponentProps {}

interface State {}

export default withRouter(ResumeContainer);
