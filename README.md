# Outline
- Prerequisits
- Install
- Run

# Prerequisits
- python 3.10.4
- venv

# Install
- Create virtual environment
```bash
python3 -m venv --prompt="venv" .venv
```

- Activate virtual environment
```bash
source .venv/bin/activate
```

- Install required modules
```bash
python3 -m pip install -r requirements/development.txt
```

# Run
```bash
cd src/
python manage.py runserver 
```
