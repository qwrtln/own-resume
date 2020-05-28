# OWN-RESUME backend

### Installation

Make sure you have Python 3.8.2+ installed on your system. It is recommended to create virtual environment for your project. Pyenv helps you manage such stuff: https://github.com/pyenv/pyenv

Assuming you have pyenv up and running with Python 3.8.2 installed, create a virtualenv:

```bash
$ pyenv virtualenv 3.8.2 my-venv-name
```

Activate your venv:
```bash
$ pyenv activate my-venv-name
```

Install requirements:
```bash
$ pip install -r requirements.txt -r requirements.dev.txt
```

And you're good to go!

### Running

Running a development version is as simple as:
```bash
$ uvicorn main:app --reload
```

Test, if you like:
```bash
$  curl localhost:8000
```

### Development
`nox` is utilized as a task runner. Install it in your venv:
```bash
$ pip install nox
```

#### Testing
`pytest` is in the requirements file, so assuming you're in the main directory, just run:
```bash
$ pytest
```
Alternatively:
```bash
$ nox -s pytest
```

#### Formatting, linting and typing
`black` as a nox session is configured to show diffs only. In order to format the code, run it by hand (it will read all the settings from `pyproject.toml`):
```bash
$ black .
```

Due to its simple configuration (just .flake8 file), run flake8 like:
```bash
$ flake8 .
```

In order to run `mypy` without specifying files or directories by hand, 
you can run it as a nox session:
```bash
$ nox -s mypy
```

#### All at once
To run pytest, black, mypy and flake8 all at once:
```bash
$ nox
```
