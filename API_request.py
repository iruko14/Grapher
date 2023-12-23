import requests

def get_categories():
    # Requesting adress
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print("request adress: https://api.escuelajs.co/api/v1/categories")

    print("--------------------------------------------------")

    # Checking status code
    print("status code: ",r.status_code)
    if r.status_code == 200:
        print("ENABLE")
    else:
        print("ERROR")

    print("--------------------------------------------------------------------------------------------------------------")

    # Getting page content
    print("page text: ",r.text)

    print("--------------------------------------------------------------------------------------------------------------")

    # Printing page content data type
    print("data type: ", type(r.text))

    print("--------------------------------------------------")

    # Translating content to json
    categories = r.json()
    # Getting categories name
    for category in categories:
        print("categories: ", category['name'])

    print("--------------------------------------------------")