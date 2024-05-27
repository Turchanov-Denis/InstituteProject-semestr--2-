import requests
import json

def print_response(response, request_text):
    print("Request:")
    print(request_text)
    print("\nResponse Code:", response.status_code)
    print("Response Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
    print("\nResponse Body:")
    print(response.text)
    print("\n" + "-" * 80 + "\n")

def save_response_to_file(response, request_text, filename):
    with open(filename, 'w') as file:
        file.write("Request:\n")
        file.write(request_text + "\n")
        file.write("\nResponse Code: " + str(response.status_code) + "\n")
        file.write("Response Headers:\n")
        for key, value in response.headers.items():
            file.write(f"{key}: {value}\n")
        file.write("\nResponse Body:\n")
        file.write(response.text + "\n")
        file.write("\n" + "-" * 80 + "\n")

def http_option(url):
    response = requests.options(url)
    request_text = f"OPTIONS {url} HTTP/1.1"
    print_response(response, request_text)
    save_response_to_file(response, request_text, 'options_response.txt')

def http_get(url, params=None):
    response = requests.get(url, params=params)
    request_text = f"GET {url} HTTP/1.1\nParams: {params}"
    print_response(response, request_text)
    save_response_to_file(response, request_text, 'get_response.txt')

def http_post(url, data=None):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    request_text = f"POST {url} HTTP/1.1\nHeaders: {headers}\nData: {json.dumps(data)}"
    print_response(response, request_text)
    save_response_to_file(response, request_text, 'post_response.txt')

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"  # Тестовый URL

    # Выполнение методов
    print("OPTIONS Request:")
    http_option(url)

    print("GET Request:")
    http_get(url, params={'userId': 1})

    print("POST Request:")
    http_post(url, data={'title': 'foo', 'body': 'bar', 'userId': 1})
