## Sample Django Project Using Postgres DB | ![Visitor Count](https://visitor-badge.glitch.me/badge?page_id=0xStryK3R.Sample-Django-Postgres-Project)

1. Setup the DB Database:
      ```sql
      CREATE DATABASE carsdb;
      CREATE USER carsadmin WITH ENCRYPTED PASSWORD 'carspass';
      GRANT ALL PRIVILEGES ON DATABASE carsdb TO carsadmin;
      ```
2. Clone Git-Repo into Local Directory.
3. Update DB credentials in _`settings.py`_ file in _`.\myproject\`_ folder to as per your own configuration.
4. Open Command Line in main directory of project.
5. Run below command inside project directory to setup environment
      ```console
      python -m venv venv
      ```
6. Activate enviroment with below command (for Windows):
      ```console
      venv\Scripts\activate
      ```
7. Run below command next to install required modules plus dependencies defined in `requirements.txt`
      ```console
      pip install -r requirements.txt
      ```
8. Migrate default/admin tables:
      ```console
      python manage.py makemigrations
      python manage.py migrate
      ```
9. Create a super user(admin) for your project:
      ```console
      python manage.py createsuperuser
      ```
      > _**Note:** This user is used to manage administration for your project via the admins console: [`/admin`](http://localhost:5000/admin/)._

10. Migrate cars tables - _`cars_car`_ and _`cars_driver`_ tables:
      ```console
      python manage.py makemigrations cars
      python manage.py migrate cars
      ```
11. Insert some data into the newly created _`cars_car`_ and _`cars_driver`_ tables.
    > _**Note:**_ _You can use sample insert queries provided in below files:_     
    > [<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/regular/file-lines.svg" width="15" height="15"> cars_car.txt](https://github.com/0xStryK3R/Sample-Django-Postgres-Project-/files/9330911/cars_car_sample_data.txt)     
    > [<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/regular/file-lines.svg" width="15" height="15"> cars_driver.txt](https://github.com/0xStryK3R/Sample-Django-Postgres-Project-/files/9330912/cars_driver_sample_data.txt)

12. Run the project:
    ```console
    python manage.py runserver 0.0.0.0:5000
    ```    
13. All Done!! [`Click Here`](http://localhost:5000/cars/1) to interact with your app:

> _**Assumptions**: Python and Postgres has been setup and running prior to starting with this project._

> _**References**: For Complete details, please refer [`How to use PostgreSQL with Django`](https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django) - the source article for this Repo._

    
