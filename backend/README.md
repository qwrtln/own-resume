# OWN-RESUME backend

## Installation

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

## Running

Running a development version is as simple as:
```bash
$ python app.py
```

