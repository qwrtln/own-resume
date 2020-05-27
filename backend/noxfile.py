import nox


requirements = [
    "-r",
    "requirements.txt",
    "pytest",
    "requests",
]
black_args = [
    "black",
    "--check",
    "--diff",
    ".",
]
mypy_args = [
    "mypy",
    "basics",
    "main.py",
    "resume",
    "work",
]


@nox.session(reuse_venv=True)
def pytest(session):
    session.install(*requirements)
    session.run("pytest")


@nox.session(reuse_venv=True)
def black(session):
    session.install("black")
    session.run(*black_args)


@nox.session(reuse_venv=True)
def mypy(session):
    session.install("mypy")
    session.run(*mypy_args)


@nox.session(reuse_venv=True)
def flake8(session):
    session.install("flake8")
    session.run("flake8")
