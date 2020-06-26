let loggedIn = false;

export function isLoggedIn(): boolean {
  return loggedIn;
}

export function logIn() {
  loggedIn = true;
}

export function logOut() {
  loggedIn = false;
}
