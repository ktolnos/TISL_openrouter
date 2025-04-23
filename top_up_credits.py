from utils import *
print(f"Adding {CREDITS_PER_MONTH} to everyone")
for row in database.itertuples():
    if row.KEY_HASH is not None:
        response = requests.get(
            f"{BASE_URL}/{row.KEY_HASH}",
            headers={
                "Authorization": f"Bearer {PROVISIONING_API_KEY}",
                "Content-Type": "application/json"
            }
        )
        data = response.json()
        usage = data['data']['usage']
        new_limit = float(usage) + float(CREDITS_PER_MONTH)

        response = requests.patch(
            f"{BASE_URL}/{row.KEY_HASH}",
            headers={
                "Authorization": f"Bearer {PROVISIONING_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "limit": new_limit
            }
        )
        if response.status_code == 200:
            print(f"Updated limit for {row.USER} to {new_limit} credits.")
        else:
            print(f"Failed to update limit for {row.USER}. Response: {response.text}")
    else:
        print(f"User {row.USER} does not have a key hash.")
