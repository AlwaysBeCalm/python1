# python1
this is the backend for [mazoon](https://github.com/DEEEMH54/m) repo

### how to run it:
* clone the repo: `git clone https://github.com/DEEEMH54/python1.git`
* then create a virtual environment (venv) `python3 -m venv venv`
* activate the environment:
  * Windows: run in cmd or powershell in same folder: `venv/Script/Activate`
  * Linux or MacOS: run in terminal in same folder: `source venv/bin/activate`
* then install the required libraries, run in terminal in same folder: `pip install -r requirements.txt`
* run the server using: `python app.py`

### how to use it:
there are some endpoints:
* `/register`: 
    this endpoint receives `fullname`, `email`, `password`, and `confirm_password` in request body
    to create a new user in the app
* `/login`:
    this endpoint receives `email`, and `password` in request body
    for user login, and return a token if provided credentials belongs to existence user.
* `/logout`
    this endpoint receives `token` in request body
    to log out the user.
* `/analyze`
    this endpoint receives `token`, and `poem` in request body
    to analyze the poem and return the result.
