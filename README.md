

Assignment
==========

change to working directory
```$ cd .```

update python packages
```$ python -m pip install -U pip setuptools wheel ```

create virtual environment
```$ python -m venv venv```

Activate virtual environment on windows
```$ venv/Scripts/activate```

Activate virtual environment on linux
```$ source venv/bin/activate```

Install python packages
```(venv) $ python -m pip install -r requirements.txt```

Create database repository
```(venv) $ flask db init```

Migration
```(venv) $ flask db migrate -m "users table"```
```(venv) $ flask db upgrade```

Setup environment. replace export with set on windows.
Don't worry about this, it is handled in .flaskenv
```(venv) $ export FLASK_APP=main.py```
```(venv) $ export FLASK_PORT=```

Start server
```(venv) $ flask run```
