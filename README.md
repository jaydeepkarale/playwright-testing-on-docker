# Playwright And Docker

This repository contains code to demo Python Playwright 🎭 and Docker🐋

The projec uses Page Object Model(POM) design pattern to implement 8 tests on 3 different pages of the test website [LambdaTest Ecommerce Playground Demo Website](https://ecommerce-playground.lambdatest.io/)

```
DockerPlaywright
├─ .gitignore
├─ docker-compose.yaml
├─ Dockerfile
├─ pages
│  ├─ accountpage.py
│  ├─ homepage.py
│  ├─ productpage.py
│  └─ __init__.py
├─ secrets.env
├─ tests
│  ├─ conftest.py
│  ├─ test_accountpage.py
│  ├─ test_homepage.py
│  ├─ test_productpage.py
│  └─ __init__.py
└─ utilities
   ├─ utilities.py
   └─ __init__.py

```

The tests written can be run on docker locally or on cloud docker grid, to control this you need to alter the ``secrets.env`` file

## Version Check

The code has been fully tested on the below versions

🐋 Docker 20.10.22, build 3a2c30b

🐍 Python 3.9.12

🧪 Pytest 7.2.1 

🎭 Playwright 1.30.0

## Env File
The ``secrets.env`` file drives the running of the tests. They have been defaulted to run on local docker but by setting the ``TEST_ENV`` parameter to cloud they can be run on cloud grids as well. For cloud grid you will also need additional username and access key which again are configured within the ``secrets.env`` file itsef

## Running the tests locally without docker
Clone the code and create a virtal environment. Install the ``requirements.txt`` and activate the virtual env, after that you can fire the below command

``pytest -v tests``

## Running the tests locally using parallelism
Clone the code and create a virtal environment. Install the ``requirements.txt`` and activate the virtual env, after that you can fire the below command
This will create 3 processes and run 3 tests at a time

``pytest -v --numprocesses 3 tests``

## Running the tests on docker

``docker build -t <image_name:tag>``

``docker run -it --env-file secrets.env image_name``