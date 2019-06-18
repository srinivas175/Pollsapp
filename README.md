# PollsApp
A simple demo project to undersatnd the basics of the Django Framework. It deals with creating a simple app "polls" to collect the votes of different questions with respective choices.
## Requirements
- Django Framework
- Virtual Environmet
## Installation
- **Virtual Environment setup**
> This site helps in setting up the [Virtual Environment](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)
- **For Django**
> pip install django
## Project Setup
1. Download and unzip [this entire repository](https://github.com/srinivas175/pollsapp) from GitHub, either interactively, or by entering the following in your Terminal.
> git clone https://<span></span>github.com<span></span>/srinivas175<span></span>/pollsapp.git
## Apps
- **[pollsapp](https://github.com/srinivas175/pollsapp/blob/master/README.md#pollsapp-1)**
- **[dashboard](https://github.com/srinivas175/pollsapp/blob/master/README.md#dashboard)**
- **[polls](https://github.com/srinivas175/pollsapp/blob/master/README.md#polls)**
## pollsapp
The default app created during the project creation. Contains important files like **settings.py** and **urls.py** 

To create pollsapp:
```python
django-admin startproject pollsapp
```
## polls
custom app that handles the core logic of the project.
> Features
- Shows the Polls questions, respective choices
- Submitting votes
- Displaying the votes

> To create polls or any custom app:
```python
django-admin startapp <appname>
```
> **Models**
  - Question - Stores the questions
  - Choice - Stores the choices for the respective question and track the votes

## dashboard
> **This is not Required**

app that handles the home page of Polls App 


