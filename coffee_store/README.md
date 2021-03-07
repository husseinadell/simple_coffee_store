### installation  
    python3 -m venv .env
    source .env/bin/activate 
    pip install -r requirements.txt
    python manage.py migrate`

### run 
    python manage.py runserver

### test APIs

coffee_machines: http://localhost:8000/api/coffee_machines/

coffee_pods: http://localhost:8000/api/coffee_pods/

# Note: you can test both in the browser and filter also