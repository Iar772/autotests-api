import time

import httpx

from tools.fakers import fake

create_user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)

login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)
time.sleep(2)
update_user_payload = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
user_id = create_user_response_data['user']['id']
get_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
update_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{user_id}",
    json=update_user_payload,
    headers=get_user_headers
)
update_user_response_data = update_user_response.json()
print('Update user data:', update_user_response_data)
print('update user data response status code:', update_user_response.status_code)