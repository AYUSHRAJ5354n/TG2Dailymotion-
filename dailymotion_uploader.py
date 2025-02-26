import requests

def upload_to_dailymotion(file_path):
    client_id = '4b8ebba0a67b86ead065'
    client_secret = 'df6256d39ab33634919703751e792b9eda135087'
    username = 'akabarbabar8@gmail.com'
    password = 'AYUSHRA5354N@'

    # Authenticate and get the access token
    auth_response = requests.post(
        'https://api.dailymotion.com/oauth/token',
        data={
            'grant_type': 'password',
            'client_id': client_id,
            'client_secret': client_secret,
            'username': username,
            'password': password,
            'scope': 'manage_videos'
        }
    )
    access_token = auth_response.json().get('access_token')

    # Upload the file to Dailymotion
    upload_response = requests.post(
        'https://api.dailymotion.com/file/upload',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    upload_url = upload_response.json().get('upload_url')

    with open(file_path, 'rb') as f:
        files = {'file': f}
        upload_file_response = requests.post(upload_url, files=files)

    return upload_file_response.json()
