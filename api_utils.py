import requests 

base_url = 'http://2million.htb/api/'
session_cookie = 'k5grue0pguiqi0qv87v5daqv3g'
session = requests.Session()
session.headers.update({'Cookie': f'PHPSESSID={session_cookie}'})


endpoints = {
    'GET': [
        'v1',
        'v1/invite/how/to/generate',
        'v1/invite/generate',
        'v1/invite/verify',
        'v1/user/auth',
        'v1/user/vpn/generate',
        'v1/user/vpn/regenerate',
        'v1/user/vpn/download',
        'v1/admin/auth',
    ],
    'POST': [
        'v1/user/register',
        'v1/user/login',
        'v1/admin/vpn/generate',
    ],
    'PUT': [
        'v1/admin/settings/update',
    ]
}

def send_request(method, endpoint, data=None):
    url = base_url + endpoint

    if method == 'GET':
        print("get")
        response = session.get(url)
    elif method == 'POST':
        print("post")
        response = session.post(url, data=data)
    elif method == 'PUT':
        print("put")
        response = session.put(url, json=data)
    else:
        raise ValueError("Unsupported HTTP method.")
    return response.text, url


def save_response(method, endpoint, response_data, url):
    filename = f'{method}_{url.replace("/", "_")}.txt'
    with open(filename, 'w') as file:
        if hasattr(response_data, 'content'):
            file.write(response_data.content.decode('utf-8'))
        else:
            file.write(response_data)
            
def parse_arguments():
    parser = argparse.ArgumentParser(description='Send HTTP requests to API endpoints')
    parser.add_argument('base_url', help='Base URL of the API')
    parser.add_argument('session_cookie', help='Session cookie value')
    parser.add_argument('--endpoints', help='Path to JSON file containing endpoints', required=True)
    return parser.parse_args()
