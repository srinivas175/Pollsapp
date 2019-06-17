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
## Apps
- **[pollsapp](https://github.com/srinivas175/pollsapp/blob/master/README.md#pollsapp-1)**
- **dashboard**
- **polls**
## pollsapp
The default app created during the project creation. Contains important files like **settings.py** and **urls.py** 

To create pollsapp:
```python
django-admin startproject pollsapp
```
## polls
custom app that handles the core logic of the project.
> **Models**
  - Question - Stores the questions
  - Choice - Stores the choices for the respective

To create polls or any custom app:
```python
django-admin startapp <appname>
```
