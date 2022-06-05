# Project Introduction

Hamrobooks is a online book buying and sharing platform where you can post your old books for sale or search for a book that you may be wiling to buy. You can post your speak on a book that you may be interested in. The platform only provides a medium for two parties to express interest, no actual transaction is done through the site. "

This site is purely educational. It is built using Django Web Framework with PostgreSQL as the database.

# Pre-requisites

- Python >= 3.6
- pip (Bundled with Python. Install if bundled version is not working)
- Postgres Database >=12

# Installation and Setup

1. Clone the project onto your machine and cd into the folder:
   ```bash
   $ git clone https://github.com/shrnsubedi/hamrobooks.git
   ```
2. Create a virtual environment in python 3 and activate it:

   ```bash
   $ pip install pipenv
   ```

   ```bash
   $ pipenv shell
   ```

   \_If activated the env_name will be appear in terminal

<br/>

4.  Install all the dependencies mentioned in the requirements.txt file:
    ```bash
    (venv)$ pipenv install
    ```

<br/>

5. Run the following command to install pre-commit hooks.

   ```bash
   (venv)$ pre-commit install
   ```

   _Due to presence of pre-commit hooks, it is not allowed to commit code with formatting errors. The errors will be listed out while trying to commit the code. Some of these errors will be formatted automatically while some may require you to fix them manually. The formatters used are black, flake8 and isort. Please follow the respective style guides while pushing your code._

<br/>

6. Create a new database in postgres. The credentials of the database must be specified in the env file in next step.

<br/>

7. Create a .env file ( hamrobooks_project/.env):

   ```
       These options are obtained while configuring the databse (Required)
       DATABASE_NAME=
       DATABASE_USER=
       DATABASE_PASSWORD=
       DATABASE_HOST=localhost
       DATABASE_PORT=5432

       Set debug=True while in development only
       DEBUG_SETTING=True

       Set a random string as secret key
       SECRET_KEY=
   ```

   _After configuration save the file_

<br/>

8. Run migrations on the database:
   ```bash
   (venv)$ python manage.py migrate
   ```

<br/>

9. Seed the database with books and a user

   ```bash
   (venv)$ python manage.py loaddata cms/fixtures/organization.json
   ```

10. Run the localserver and visit ( 127.0.0.1:8000 )

```bash
(venv)$ python manage.py runserver
```

11. To commit your changes checkout a branch from the master branch and push.
