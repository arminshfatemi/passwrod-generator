# Password generator
A Password generator built with python tkinter

### Features
1. Copy generated password to clipboard with a button
2. You can choose the length of your password 
3. You can choose the level of generated password
4. An Error Entry to show the error 


### Password Levels 
 1. weak : its just lowercase Characters
 
 2. medium : its numbers and lowecase Characters
 
 3. strong : lowercase ,uppercase ,numbers Characters
 
 4. Excellent : lowercase ,uppercase ,numbers and symbols Characters



### How to Run

1. First clone the project and cd to project 
```commandline
git clone <url of the project>
cd Password-generator
```
2. Make a python virtual env
```commandline
python3 -m venv <name of your venv>
```
3. Activate your venv
#### on linux
```commandline
source ./venv/bin/activate
```
#### on windows
```commandline
venv/bin/activate
```

4. Install the python packages
```commandline
pip install -r requirements.txt
```
5. Run the file
```commandline
python password-generator.py
```

### Error
if you have error like this :

ERROR: Could not find a version that satisfies the requirement tkinter (from versions: none)

ERROR: No matching distribution found for tkinter

first make sure you have installed packages and venv is activated 
if it didn't fixed do below command 

```commandline
 sudo dnf install python3.<your version>-tkinter  
```

and i hope it fixed 

Enjoy.

