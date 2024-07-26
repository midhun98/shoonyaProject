### Step 1: Clone the Repository

```sh
git clone https://github.com/midhun98/shoonyaProject.git
cd shoonyaProject
```

### Step 2: Create the Virtual Environment

```sh
python -m venv venv
source venv\Scripts\activate.bat
```

### Step 3: Install the requirement

```sh
pip install -r requirements.txt
```

### Step 4: Create the .env in root directory and add the following line 
Change the variables accoring to your configurations
```sh
ENGINE=django.db.backends.postgresql
NAME=shoonya_DB
DB_USER=postgres
PASSWORD=root
HOST=localhost
PORT=5432
```
### Step 5: Finally Run the server

```sh
python manage.py runserver
```
