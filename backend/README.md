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

And your good to go!

### Running

Running a development version is as simple as:
```bash
$ python app.py
```

Test, if you like:
```bash
$  curl localhost:5000
"Hello, World!"
```

### Development

#### Testing
`pytest` is in the requirements file, so assuming you're in the main directory, just run:
```bash
$ pytest
```

#### Formatting and typing
`nox` is utilized as a task runner. Install it in your venv:
```bash
$ pip install nox
```
And then run pytest, black and mypy all at once:
```bash
$ nox
```
`black` is configured to show diffs only. In order to format the code, run it by hand (it will read all the settings from `pyproject.toml`):
```bash
$ black .
```

In order to run `mypy` without specifying files or directories by hand, 
you can run it as a nox session:
```bash
$ nox -s typing
```
