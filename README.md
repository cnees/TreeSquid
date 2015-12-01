# TreeSquid


How to run locally
-------------------  
1. Set up virtual python environment for Django (I found this meathod to be the simplest way of installing Django)
  - Install pip with following this guide: http://pip.readthedocs.org/en/stable/installing/.  
  - Install virtualenv: https://virtualenv.readthedocs.org/en/latest/installation.html.
  - In the root directory, TreeSquid, run ```virtualenv venv```. This will create a new directory within TreeSquid that's ingored with in .gitnore file. Connect to this virtual environment by running ```source venv/bin/activate```. You'll need to do this anytime you want to run Django code. To disconnect with the virtual environment, run ```deactivate```.
  - To install the required Django utilities, run ```pip install django-toolbelt```.
2.  Setup local Postgres DB for TreeSquid 
  - Download, install, and setup Postgres: http://www.postgresql.org/download/.
  - Connect to Postgres, ```sudo su - postgres``` 
  - Create a new database with any name you like, ```createdb dbname``` 
  - Create a new user with any name you like, ```createuser username -P``` 
  - To grant the user access to the database, first enter the Postgres CLI with ```psql```, then run  
  ```GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;```
3.  Create local_settings.py  
  - The settings.py file is configured to work on Herkoku. To run the project locally, you'll need to add a local_settings.py file. 

