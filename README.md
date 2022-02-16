# Calculator App
Simple Django based Calculator web-app following BODMAS.

# Expected Project Features:
    • Calculator follwoing bodmas
    • Custom User Login/Logout & Registration using Django Rest Framework
    • Dashboard to view history of expressions & their results
    
# Setup and Run Locally:
1. Clone the repo
2. Set up a virtual environment with requiements.txt
3. Change directory to:  calculator
4. Create superuser (optional) 
    `python manage.py createsuperuser `
5. Make migrations and migrate to setup database :
    ` python manage.py makemigrations` 
    `python manage.py migrate `
6. Run the following command:
    ` python manage.py runserver `
7. Visit http://127.0.0.1:8000/<endpoint> to view different end-points metioned below

# Test Endpoints

1. To register a new user : http://127.0.0.1:8000/api/register/
    
    
2. To view Client/User List visit: http://127.0.0.1:8000/api/client/
    
    
3. To view Calculator: http://127.0.0.1:8000/calculation/  
   
    

