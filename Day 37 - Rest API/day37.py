# @author   Lucas Cardoso de Medeiros
# @since    08/08/2022
# @version  1.0

# Pixela

from datetime import datetime
import requests


USERNAME = "zedlucas"
TOKEN = "12345678910"
GRAPH_ID = "graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

graph_header = {
    "X-USER-TOKEN": TOKEN
}


def login(token, username):
    """Login"""
    login_params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    return requests.post(url=PIXELA_ENDPOINT, json=login_params)


def create_graph(username, id, name, unit, type, color):
    """Create graph"""
    graph_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs"
    graph_config = {
        "id": id,
        "name": name,
        "unit": unit,
        "type": type,
        "color": color
    }
    return requests.post(url=graph_endpoint, json=graph_config, headers=graph_header)


def add_pixel(username, id, date, quantity):
    """Add new pixel value to the graph"""
    if date == "today":
        date = datetime.today().strftime('%Y%m%d')
    pixel_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{id}"
    pixel_params = {
        "date": date,
        "quantity": quantity,
    }
    return requests.post(url=pixel_endpoint, json=pixel_params, headers=graph_header)


def update_pixel(username, id, date, quantity):
    """Update pixel value from given date"""
    if date == "today":
        date = datetime.today().strftime('%Y%m%d')
    pixel_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{id}/{date}"
    pixel_params = {
        "quantity": quantity,
    }
    return requests.put(url=pixel_endpoint, json=pixel_params, headers=graph_header)


def delete_pixel(username, id, date):
    """Delete pixel from given date"""
    if date == "today":
        date = datetime.today().strftime('%Y%m%d')
    pixel_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{id}/{date}"
    return requests.delete(url=pixel_endpoint, headers=graph_header)


# response = login(token=TOKEN, username=USERNAME)
# print(response.text)
#
# response = create_graph(username=USERNAME, id=GRAPH_ID, name="Cardio Academia", unit="Km", type="float", color="sora")
# print(response.text)
#
# response = add_pixel(username=USERNAME, id=GRAPH_ID, date="today", quantity="3.3")
# print(response.text)
#
# response = update_pixel(username=USERNAME, id=GRAPH_ID, date="today", quantity="3.7")
# print(response.text)
#
# response = delete_pixel(username=USERNAME, id=GRAPH_ID, date="today")
# print(response.text)

# Daily update
success = False
while not success:
    response = add_pixel(username=USERNAME, id=GRAPH_ID, date="today", quantity=input("Km na esteira hoje: "))
    success = response.json()["isSuccess"]
    print(response.text)
