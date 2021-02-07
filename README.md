# The BankingAPI

- ### Installation
- create a directory and clone projects in it.
    - create a virtual environment and activate it.
        ```
        - python3 -m venv venv
        - source venv/bin/activate
        ```
    - and after all the changes in models.py files you should run the following commands:
       ```
        pip3 install -r requirements.txt
        Create your secrets file using settings/secrets.py.template file and write your credentials into it.(* if you are using prod.py file configure your postgres settings)
        python3 manage.py makemigrations main & python3 manage.py migrate
        python3 manage.py runserver
       ```
- To create an admin user:
    ``` 
    python3 manage.py createsuperuser 
    ```
    
- To run in the localhost:
    ```
    python3 manage.py runserver
    ```
- ## API
    - To list all the accounts:
        - `accounts/`
        
    - To get the detail of a account:
        - `accounts/{{id}}/`
        
    - To list all the customers:
        - `customers/`
        
    - To get the detail of a customer:
        - `customer/{{id}}/`
           
    - To list all the transfers:
        - `transfers/`
        
    - To get the detail of a transfers:
        - `transfers/{{id}}/`

    - To add the new of a customer:
        - `customer/`
        - post name parameter.
        
    - To add the new of a accounts:
        - `accounts/`
        - post  parameters as customer_id,amount.
    
    - To add the new transfer:
        - `transfers/`
        - post  parameters as from_account, to_account,amount.
     
    - To see all others api, documentation:
        - `docs/`
        
