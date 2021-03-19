## Requirements

* Python 3.9+ isntalled
* NodeJs v12.18.4+ installed

## Backend
# To Launch the Backend with virtual enviroment
cd backend
python -m venv .env

* linux
source .env/bin/activate 

* windows
.\.env\Scripts\activate

pip install -r requirements
cd technical_test
python manage.py runserver

# To Launch the Backend without virtual enviroment
cd backend
pip install -r requirements
cd technical_test
python manage.py runserver

## Frontend
# To launch

cd frontend
npm install
ng serve
Navigate to `http://localhost:4200/`
