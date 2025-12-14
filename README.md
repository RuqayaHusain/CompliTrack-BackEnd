# Python FastAPI Serializers and Controllers Lab Solution

## About

This repo contains the solution code for the [Python FastAPI Serializers and Controllers Lab](https://pages.git.generalassemb.ly/modular-curriculum-all-courses/python-fastapi-serializers-and-controllers-lab/canvas-landing-pages/fallback.html)

## Getting Started

1. Fork and clone this repo.

2. Navigate into the project directory:

```sh
 cd python-fastapi-serializers-and-controllers-lab-solution
```

3. Install dependencies (this also creates the virtual environment if it doesn’t exist):

```sh
 pipenv install
```

4. Activate the virtual environment:

```sh
 pipenv shell
```

5. Set up your PostgreSQL database:

   - Ensure PostgreSQL is installed and running on your machine.
   - Create a database named `teas_db` if it does not already exist:

```bash
createdb teas_db
```

6. Open the application in Visual Studio Code:

```bash
code .
```

7. The database connection string is defined in the `config/environment.py` file:

```python
db_URI = "postgresql://<username>@localhost:5432/teas_db"
```

> _Modify your database connection string to use your username as the `<username>`._

8. Seed the database with initial data:

   - Run the `seed.py` file to reset the database by dropping existing tables and repopulating it with starter data:

```bash
pipenv run python seed.py
```

> You should see output indicating the database was successfully seeded. If there are any errors, check the `db_URI` in the `config/environment.py` file.

9. Start the development server:

```bash
pipenv run uvicorn main:app --reload
```

> You should now have the app running. Visit [`http://127.0.0.1:8000`](http://127.0.0.1:8000) in your browser to confirm it’s working.

10. Now you can test each endpoint using FastAPI’s built-in documentation.

> Navigate to FastAPI Documentation: Open [`http://localhost:8000/docs`](http://localhost:8000/docs) in your browser.

<br>

### Troubleshooting PostgreSQL

- The database connection string is defined in the `config/environment.py` file:

  ```python
  db_URI = "postgresql://<username>@localhost:5432/teas_db"
  ```

- Ensure your PostgreSQL instance is configured to allow connections with the provided credentials.
- **_Modify your database connection string to use your username as the `<username>`._**

#### Setting Up a User in PostgreSQL

To connect to a specific PostgreSQL user, use the following command:

```sh
psql -U <username>
```

#### Handling "Role Does Not Exist" Error

If you see this error:

```sh
Error: FATAL: role "<username>" does not exist
```

it means that the specified user does not exist in PostgreSQL.

#### Creating a New PostgreSQL User

To create the user, run the following command inside `psql`:

```sql
CREATE ROLE "<username>" WITH LOGIN PASSWORD 'your_secure_password';
```

> 🔹 **Replace** `<username>` with your desired username and **choose a secure password**.

This will allow you to connect using one of the following database connection strings:

#### Connection Strings:

If **no password is required**:

```python
db_URI = "postgresql://<username>@localhost:5432/teas_db"
```

If **a password is required**:

```python
db_URI = "postgresql://<username>:<your_secure_password>@localhost:5432/teas_db"
```

This ensures that PostgreSQL correctly authenticates and allows access to the `teas_db` database.
