# supplement-store

## Project setup

### Creates virtual environment

```
python -m venv ~/envs/flask
```

### Activates virtual environment

```
. ~/envs/flask/bin/activate
```

### Installs dependencies

```
(flask) pip install -r requirements.txt
```

### Creates database tables (schema must be created manually)

```
(flask) python3 db_initializer.py
```

### Starts flask application

```
(flask) flask run
```
