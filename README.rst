# Pico y Placa Predictor

This repository based on the date, time and license plate number tells the users if their cars can or can not be on the road according to the restrictions of the Municipality.

## Setup Process

This project was developed and tested with python 3.7 so this python version is recommended to use.
First, you need to install pipenv for python 3.7:


```shell
pip3 install pipenv
```
Inside the project folder and with the Pipfile in place you need to run:
```
pipenv install --dev
```
This command will install both the development and production packages into a new virtual environment for a developer to work with this repository.

To install a new package for development purposes run:
```
pipenv install -dev package_name
```
To install a new package for dependency (production) purposes run:
```
pipenv install package_name
```
## Running locally
You can deploy the flask server locally by running the following command:

`python3.7 src/index.py`
