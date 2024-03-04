# Python Flask Web App

This application is an example to run on a flet of ec2 instances to create an autoscaling group behind an application load balancer

## Pre-requisites

- Python 3.7 and 3.9
- Flask
- Pip
- Pyenv (not required but highly recommended)


## Installation

Once you have installed python the first step is to create a virtual environment. Python allows you to create a folder in which you can store all the libraries used by your proyect.

```bash
python -m venv .env
```
 I strongly reccomend to create this folder at the root level of the project

 After create the virtual env, the next step is to activate

 ```bash
source .env/bin/activate
```

### Install project dependencies

To setup all required dependencies execute:

 ```bash
pip install -r requirements.txt
```
### Package for non-development env
To install and deploy in any web server with python just pick the page inside of dist dir
```
python -m build --wheel
```

In the new env install the whl package with this command:
```
pip install app-1.0.0-py3-none-any.whl
```

### Run Webapp
 ```bash
flask run
```
The above command will run and app instance on port 5000, so, you can check it on localhost:5000/

### Run Webapp whit waitreess server
 ```bash
waitress-serve --call --host=0.0.0.0 'app:create_app'
```
The above command will run and app instance on port 5000, so, you can check it on localhost:5000/

