import requests
#constants

world_filter="qui"

#HTTP request

resp = requests.get("https://jsonplaceholder.typicode.com/todos")

if resp.status_code == 200:

    data = resp.json()
    title_list = [todo ["title"] for todo in data]
    filtered_titles = [title for title in title_list if world_filter in title.split()]
    print("Filtered Titles:")
    for title in filtered_titles:
        print(f"- {title}") #use f-string to format and print all the filtered titles

    #type checking the list
    if all(isinstance(title, int) for title in filtered_titles):
        print("There is at least one INT data type in the list")
    else:
        print("The list contains no INT data type")
else:
    print("HTTP Get request failed, status code:", resp.status_code)