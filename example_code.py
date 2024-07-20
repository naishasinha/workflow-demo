from dotenv import load_dotenv
import os

load_dotenv()

def reverse_array(array):
    return array[::-1]

def get_secrets():
    secret_value = os.getenv('SECRET_KEY')
    return secret_value
