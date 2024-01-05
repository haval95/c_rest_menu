# Restaurant Menu

# Running the Project

To run the project, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/haval95/c_rest_menu.git
    ```

2. **Activate the Virtual Environment:**
    ```bash
    cd <project folder>
    pipenv shell
    ```

3. **Install Dependencies:**
    ```bash
    pipenv install
    ```

4. **Run the Application:**
    ```bash
    cd c_rest_menu
    python manage.py runserver
    ```

This sequence of steps will clone the repository, set up the virtual environment, install dependencies, and run the application locally.


# API END POINTS

 **requires username and password for user authentication**
```bash
 http://127.0.0.1:8000/api/token/
```
**requires username and password and email for user registration**
 ```bash
 Http://127.0.0.1:8000/auth/users/
 ```
**to show bookings and also post bookings providing name, no_guests, date**
 ```bash
http://127.0.0.1:8000/api/bookings/
 ```

    
