from utils import *

users_without_token = database[database['KEY_HASH'].isnull()]['USER']
for user in users_without_token:
    token_label = user.replace(" ", "_").replace(".", "_").replace("@", "_")
    response = requests.post(
        BASE_URL,
        headers={
            "Authorization": f"Bearer {PROVISIONING_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "name": user,
            "label": token_label,
            "limit": CREDITS_PER_MONTH
        }
    )
    key_hash = response.json()['data']['hash']
    key = response.json()['key']
    database.loc[database['USER'] == user, 'KEY_HASH'] = key_hash
    database.loc[database['USER'] == user, 'KEY'] = key

    print(user, key)
database.to_csv('database.csv', index=False)