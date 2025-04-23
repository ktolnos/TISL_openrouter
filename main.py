import requests

with open('MANAGEMENT_KEY') as f:
    PROVISIONING_API_KEY = f.read().strip()
BASE_URL = "https://openrouter.ai/api/v1/keys"

# Create a new API key
response = requests.post(
    f"{BASE_URL}/",
    headers={
        "Authorization": f"Bearer {PROVISIONING_API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "name": "Test",
        "label": "test-123",
        "limit": 5  # Optional credit limit
    }
)

response
# # Get a specific key
# key_hash = "<YOUR_KEY_HASH>"
# response = requests.get(
#     f"{BASE_URL}/{key_hash}",
#     headers={
#         "Authorization": f"Bearer {PROVISIONING_API_KEY}",
#         "Content-Type": "application/json"
#     }
# )
# # Update a key
# response = requests.patch(
#     f"{BASE_URL}/{key_hash}",
#     headers={
#         "Authorization": f"Bearer {PROVISIONING_API_KEY}",
#         "Content-Type": "application/json"
#     },
#     json={
#         "name": "Updated Key Name",
#         "disabled": True  # Disable the key
#     }
# )
# # Delete a key
# response = requests.delete(
#     f"{BASE_URL}/{key_hash}",
#     headers={
#         "Authorization": f"Bearer {PROVISIONING_API_KEY}",
#         "Content-Type": "application/json"
#     }
# )