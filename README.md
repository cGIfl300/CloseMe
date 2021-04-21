#CloseMe

An application to kill unwanted applications. By default, it is set up to
scan your running applications list each 5 seconds and kill the ones on  
  
`Forbidden_Apps = [
    "hexchat.exe",
]`
  
You can modify these values as you wish.  
This software is Windows Only.

## Deployment

### Installing python

You may better following the instructions
from [https://www.python.org/](https://www.python.org) .

### Download the software

You can download it
from [this git depository](https://github.com/cGIfl300/).

### Installing a venv

Open a shell and go inside the project folder, then use :  
`python -m venv env`

### Activate a venv

To activate the venv, use:  
`source env/bin/activate`  
or for Microsoft Windows users:  
`env/Scripts/activate.bat`

### Install required libs

To install the required libs use:  
`pip install -r requirements.txt`  

##Use  
python main.py