import React from "react";
import "./App.css";
import { isLoggedIn } from "./auth/AuthService";
import ResumeContainer from "./resume/ResumeContainer";
import LoginContainer from "./login/LoginContainer";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

function App() {
  return (
    <div className="App">
      <div>
        <Router>
          <Switch>
            <Route path="/login" exact={true}>
              <LoginContainer />
            </Route>
            <Route
              path="/"
              exact={true}
              render={({ location }) =>
                isLoggedIn() ? (
                  <ResumeContainer />
                ) : (
                  <Redirect to={{ pathname: "/login" }} />
                )
              }
            ></Route>
          </Switch>
        </Router>
      </div>
    </div>
  );
}

export default App;
