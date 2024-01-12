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
<br /><br />
**AUTHENTICATION AND REGISTRATION**
<br /><br />
<code >POST</code> - AUTHENTICATION - [USERNAME, PASSWORD]
```bash
 http://127.0.0.1:8000/api/token/
```
<code >POST</code> - REGISTRATION - [USERNAME, PASSWORD, EMAIL]
 ```bash
 Http://127.0.0.1:8000/auth/users/
 ```
<br /><br />
**CATEGORIES AND MENU ITEMS**
<br />
<code >GET</code> - GATEGORIES AND MENUITEMS  - PUBLIC
 ```bash
    http://127.0.0.1:8000/api/categories/
 ```
<code >GET</code> - SINGLE CATEGORY AND MENUITEMS  - PUBLIC
 ```bash
    http://127.0.0.1:8000/api/categories/[ID]
 ```

<code >POST</code> - INSERT  CATEGORY   [NAME, NAME_LANG]
 ```bash
    http://127.0.0.1:8000/api/categories/
 ```
<br /><br />
**CART**
<br />
<code >GET</code> - CART ITEMS - AUTHENTICATION REQUIRED
 ```bash
   http://127.0.0.1:8000/api/cart/
 ```
<code >POST</code> - INSERT AN ITEM TO CART - [QUANTITY, MENU_ITEM_ID]
 ```bash
   http://127.0.0.1:8000/api/cart/
 ```
<br /><br />
**RESERVATION**
<br />

<code >POST</code> - RESERVING A TABLE
 ```bash
    http://127.0.0.1:8000/api/reservation/
 ```
 ```bash
  {
    "table_id": 1,
    "reservation_time": "2024-01-13T06:31:00Z",
    "for_how_long": "01:02:00",
}
 ```

<code >GET</code> -  RESERVED TIMES
 ```bash
    http://127.0.0.1:8000/api/reservation/
 ```
 ```bash

