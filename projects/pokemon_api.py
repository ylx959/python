import requests

base_url="https://pokeapi.co/api/v2"

def get_info(name):
    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url)

    if response.status_code==200: #200代表請求成功
        info_data=response.json() #把回傳的json轉成字典
        return info_data
    else:
        print("Failed")
        return None
    
name=input("Enter the character name:").lower()

data=get_info(name)

if data: #查詢失敗時data是None
    print(f"Name:{data["name"].capitalize()}")
    print(f"ID:{data["id"]}")
    print(f"Height:{data["height"]}")



