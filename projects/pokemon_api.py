import requests

base_url="https://pokeapi.co/api/v2/"

def get_info(name):
    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url)

    if response.status_code==200:
        info_data=response.json()
        return info_data
    else:
        print("Failed")
        return None
    
name=input("Enter the character name:")

data=get_info(name)

print(f"Name:{data["name"].capitalize()}")
print(f"ID:{data["id"]}")
print(f"Height:{data["height"]}")



