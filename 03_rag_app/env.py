import os
from dotenv import load_dotenv, find_dotenv

def get_env_variable(var_name: str) -> str:
    env_path = find_dotenv()
    if not env_path:
        raise FileNotFoundError(".env file not found.")

    load_dotenv(env_path)
    value = os.getenv(var_name)
    if value is None:
        raise ValueError(f"{var_name} not found in .env file.")
    return value
