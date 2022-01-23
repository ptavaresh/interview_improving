# Python interview - Improving

API created in Django which interacts with two endpoints (see below), search endpoint will take one numeric value that will be compared with a list of values stored in Django-ORM Class using model serializer an view, otherwise the search endpoint is a custom endpoint created to just call the amount values stored in sqlite DB and does the calculations.

## endpoints
 http://localhost:8000/search/ [POST]
 - This search endpoint take as request a json object with a amount as key and a number as value.
![search](https://github.com/ptavaresh/interview_improving/blob/main/img/search.PNG)

 http://localhost:8000/amounts/ [GET] [POST]
 - This endpoint can create new amounts rows using Django-ORM and can get all stored values.
 ![amount](https://github.com/ptavaresh/interview_improving/blob/main/img/amount.PNG)

## requeriments
- Python 3.6 or higher
- pip
- virtualenv

 ## Steps to run local API
- clone the repository
- Create your virtual environment
  `python -m venv venv`

- Activate your virtual environment
  `source venv/Scripts/activate`

- run below commands in project path
    - Install pip requiriments.txt
        
        `pip install -r requirements.txt`
        
    - Run django server

        `python manage.py runserver`
