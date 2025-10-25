from Customer.views.customerLogin import customer_login
from Customer.views.customerRegister import customer_register
from auth.views.createToken import create_token_for_user

def handle_customer_login(email: str, password: str):
    user_data = customer_login(email, password)
    return create_token_for_user(user_data)

def handle_customer_register(email: str, password: str, name: str):
    return customer_register(email, password, name)