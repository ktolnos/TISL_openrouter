import requests
import pandas as pd

with open('MANAGEMENT_KEY') as f:
    PROVISIONING_API_KEY = f.read().strip()
BASE_URL = "https://openrouter.ai/api/v1/keys"

database = pd.read_csv('database.csv')

CREDITS_PER_MONTH = 5