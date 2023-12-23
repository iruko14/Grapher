import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print("request adress: https://api.escuelajs.co/api/v1/categories")
    print("--------------------------------------------------")
    print("status code: ",r.status_code)
    if r.status_code == 200:
        print("ENABLE")
    else:
        print("ERROR")
    print("--------------------------------------------------------------------------------------------------------------")
    print("page text: ",r.text)
    print("--------------------------------------------------------------------------------------------------------------")
    print("data type: ", type(r.text))
    print("--------------------------------------------------")
    categories = r.json()

    for category in categories:
        print("categories: ", category['name'])
    print("--------------------------------------------------")