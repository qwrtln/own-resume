import nox


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
    session.run("poetry", "install", external=True)
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
