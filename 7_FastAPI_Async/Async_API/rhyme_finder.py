import asyncio
import time
import dotenv
import os
import json 
import requests



async def rhymes_finder(user_input_word):
    print("....... rhyme started ....... ")
    url = f"https://rhyming.ir/api/rhyme-finder?api={rhyme_API_KEY}&w={user_input_word}&sb=1&mfe=2&eq=1"
    response = requests.request("GET", url)
    dictionary = json.loads(response.text)
    rhymes_list = []
    for item in dictionary["data_items"] :
        rhymes_list.append(item["word"])    
    print("rhymes_list : "  , rhymes_list) 
    await asyncio.sleep(1)
    print("....... rhyme finished .......")

# -------------------------------------------------------------------------------------------------------

def get_states_list():
    url = "https://iran-locations-api.vercel.app/api/v1/fa/states"
    response = requests.request("GET", url)
    states_list = json.loads(response.text)
    print("getting states list finished " ) 
    return states_list


def get_cities_list(state_id):
    url = f"https://iran-locations-api.vercel.app/api/v1/fa/cities?state_id={state_id}"
    response = requests.request("GET", url)
    state_info = json.loads(response.text)
    cities_list = state_info["cities"]
    print("getting cities list finished") 
    return cities_list


def state_id_finder(state_name , state_list):
    for state in state_list : 
        if state_name == state["name"] :
            state_id =  state["id"]
            print("state_id : " , state_id)  
            return state_id


def find_city_info(city_name , cities_list):
    for city in cities_list :
        if city["name"] == city_name :
            print("finding city info finished : " , city ) 
            return city


async def get_coordinates(state_name , city_name):
    print("🔷 get_coordinate started  .... 🔷")
    states_list = get_states_list()
    state_id = state_id_finder(state_name , states_list)
    cities_list =  get_cities_list(state_id)
    city_info = find_city_info(city_name , cities_list)
    await asyncio.sleep(1)
    print("🔺 latitude : " ,  city_info["latitude"]  )
    print( "🔺 longitude  : " , city_info["longitude"] )
    print(f"🔷 get_coordinate finished ....🔷")


async def main():
    await asyncio.gather(rhymes_finder(user_input_word="آدینه") , get_coordinates(state_name="خوزستان" , city_name="ايرانشهر") )
    print("main ended")



if __name__ == "__main__" :
    dotenv = dotenv.load_dotenv()
    rhyme_API_KEY = os.getenv("rhyme_APIkey")
    
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    duration_of_main_function = end_time - start_time
    print(f"executed in {duration_of_main_function} seconds ")
