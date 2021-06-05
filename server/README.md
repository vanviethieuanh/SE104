## For Development

### Running

1.  🙂 Windows

```sh
# 🗻 Create environment
python -m venv env
.\env\Scripts\activate

# ⚙ Setup environment
pip install -r .\requirements.txt

# 🏃‍♂️ Run server
python .\manage.py runserver
```

2.  🐧 Linux

```sh
# 🗻 Create environment
python3 -m venv env
source env/bin/activate

# ⚙ Setup environment
pip3 install -r .\requirements.txt

# 🏃‍♂️ Run server
python3 .\manage.py runserver
```

### Testing

```sh
# on Linux
python3 manage.py test

# on Windows
python .\manage.py test
```
