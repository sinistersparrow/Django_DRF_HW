import requests


def client():
    token_h = "Token 8471f5fec5d20bec9649a684beb4d9ae3b0370f0"
    # credentials = {"username": "admin", "password": "admin"}
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)

    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles", headers=headers)

    print("Status Code:  ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()


