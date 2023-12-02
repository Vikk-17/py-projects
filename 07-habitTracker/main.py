import requests
from datetime import datetime


def main():
    today = datetime(year=2023, month=11, day=28)
    formatted_date = today.strftime("%Y%m%d")

    TOKEN = "myTokenOFXZX"
    # create the user account
    parameters = {
        "token":TOKEN,
        "username":"venom101",
        "agreeTermsOfService":"yes",
        "notMinor":"yes",
    }

    #pixela endpoint
    pixela_endpoint = "https://pixe.la/v1/users"
    graph_endpoint = f"{pixela_endpoint}/venom101/graphs"

    graph_config = {
        "id": "developing200",
        "name": "Python",
        "unit": "commit",
        "type": "float",
        "color": "shibafu",
    }

    headers = {
        "X-USER-TOKEN": TOKEN
    }
    

    # r = requests.post(url=pixela_endpoint, json=parameters)
    # print(r.text)

    # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    # print(response.text)


    # post value to the graph
    my_graph_endpoint = "https://pixe.la/v1/users/venom101/graphs/developing200"
    today_work_config = {
        "date": formatted_date,
        "quantity": "8",
    }

    # r = requests.post(url=my_graph_endpoint, json=today_work_config, headers=headers)
    # print(r.text)

    # update data
    data_config = {
        "quantity": "8"
    }
    update_endpoint = "https://pixe.la/v1/users/venom101/graphs/developing200/20231201"

    r = requests.put(url=update_endpoint, json=data_config, headers=headers)
    print(r.text)

if __name__ == "__main__":
    main()