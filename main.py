import requests
import datetime
GENDER = "male"
WEIGHT_KG = 50
HEIGHT_CM = 155
AGE = 37

global date_today
global time_today

APP_ID =  "23964751"
APP_KEY = "2249b99922edd40e5e4e4a3e36d92964"
REMOTE_USER_ID = "0"
#x-app-id
#x-app-key
#x-remote-user-id

headers = {
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY,
    #"x-remote-user-id":REMOTE_USER_ID
}


my_config = {
    "query":"Ran 2 km, swam 10m",
    #"gender": GENDER,
    #"weight_kg": WEIGHT_KG,
    #"height_cm": HEIGHT_CM,
    #"age": AGE
}

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=endpoint, headers=headers, json= my_config)
reply = response.json()
#print(reply)

to_write = reply["exercises"]
#print(to_write)
final_dict = []

for i in to_write:
    my_dict = {}
    my_dict["user_input"] = i["user_input"]
    my_dict["duration_min"] = i["duration_min"]
    my_dict["nf_calories"] = i["nf_calories"]
    final_dict.append(my_dict)

print(final_dict)
date_today = datetime.datetime.now().strftime("%d/%m/%Y")
time_today = datetime.datetime.now().strftime("%H:%M:%S")

print(date_today)
print(time_today)

sheety_endpoint = "https://api.sheety.co/dfdf5f2d10b9bb5354081d1eaa3daf92/workoutTracker/workouts"

for i in final_dict:
    sheety_config = {
        "workout": {
            "date": date_today,
            "time": time_today,
            "exercise": i["user_input"],
            "duration": i["duration_min"],
            "calories": i["nf_calories"]
        }
    }
    # print(sheety_config)
# for exercise in reply["exercises"]:
#     sheet_inputs = {
#         "workout": {
#             "date": date_today,
#             "time": time_today,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }
    response = requests.post(url=sheety_endpoint, json = sheety_config)
    print(response.text)
