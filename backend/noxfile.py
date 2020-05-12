import nox


requirements = [
    "-r",
    "requirements.txt",
    "pytest",
    "Flask-Testing",
]
black_args = [
    "black",
    "--check",
    "--diff",
    ".",
]
mypy_args = [
    "mypy",
    "resources/",
    "models",
    "app.py",
]


@nox.session(reuse_venv=True)
def tests(session):
    session.install(*requirements)
    session.run("pytest")


@nox.session(reuse_venv=True)
def formatting(session):
    session.install("black")
    session.run(*black_args)


@nox.session(reuse_venv=True)
def typing(session):
    session.install("mypy")
    session.run(*mypy_args)
