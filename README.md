# Requirements

* Python 3.9+ isntalled
* NodeJs v12.18.4+ installed

# Backend
## To Deploy the Backend with virtual enviroment

```bash
cd backend
python -m venv .env
```
* linux
```bash
source .env/bin/activate 
```

* windows
```powershell
.\.env\Scripts\activate
```

```bash
pip install -r requirements
cd technical_test
python manage.py runserver
```

## To Deploy the Backend without virtual enviroment
```bash
cd backend
pip install -r requirements
cd technical_test
python manage.py runserver
```
# Frontend
## To Deploy
```bash
cd frontend
npm install
ng serve
```
Navigate to [http://localhost:4200/](http://localhost:4200/)

