## Enlabeler System(EPMS)


# Installation on Windows, Mac and Unix using:

- Download Python from the [official Python site](https://www.python.org/downloads/release/python-361/)
- Install Python and add it to environmental variables
- On your develop directory, create a virtual environment. Can follow the this documentation / guidelines:
https://virtualenv.pypa.io/en/stable/userguide/

- Activate the environment, guidelines provided in the link above. Here is an example you would type on the command line:
```
path\to\env\Scripts\activate
```
- It's entirely up to the developer where they wish to place the virtual environment. It's recommend you create a
directory and label something like 'venvs' and create the environments there for each project. Along side the
'venv' directory, will be the project directories.
- Along side the virtual environments directory e.g' 'venvs' clone the project.
- At this step, you should have the virtual environment and it should be activated. Next to the root of the virtual
environments you will have the project you recently cloned.


# Setting up environment
```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```
# Running application
```
cd enterprise_performance_management
python3 manage.py migrate
```
Create a super user and follow the instructions:
```
python3 manage.py createsuper
```
Finally, run the server:
```
python3 manage.py runserver
```
The app should hosted on [localhost:8000](localhost:8000).

# Docker

```
docker build .
```
```
docker-compose build
```


## Application Overview

- This is a test

There are few pages. 
These include:

- Dashboard
- Add your availibilty
- Generate pics
- Signup
- Login


# Dashboad Module
![alt text](https://github.com/lukhanyo21/testing/blob/main/src/readme_pics/dashboard.png)

# Time
![alt text](https://github.com/lukhanyo21/testing/blob/main/src/readme_pics/avail.png)

# Picmix
![alt text](https://github.com/lukhanyo21/testing/blob/main/src/readme_pics/picmix.png)

# Signup
![alt text](https://github.com/lukhanyo21/testing/blob/main/src/readme_pics/signup.png)

# Login

![alt text](https://github.com/lukhanyo21/testing/blob/main/src/readme_pics/sign.png)

# Design
![alt text](https://github.com/lukhanyo21/testing/blob/main/src/readme_pics/Design.png)

# ERD
![alt text](https://github.com/lukhanyo21/testing/blob/main/src/readme_pics/erd.png)

