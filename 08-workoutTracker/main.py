import requests
from dotenv import load_dotenv
import os
from datetime import datetime


def main():
    print(postToSheet(getNutrition()))


def getNutrition() -> dict:
    today_date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%X")

    load_dotenv()
    exercise_text = input("Tell me which exercises you did: ")
    endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    headers = {
        "x-app-id": os.getenv("API_ID"),
        "x-app-key": os.getenv("API_KEY")
    }
    
    parmeters = {
        "query": exercise_text
    }

    resp = requests.post(url=endpoint, headers=headers, json=parmeters)
    
    results = resp.json()

    nutrition_dict = {
        "date": today_date,
        "time": now_time,
        "exercise": (results["exercises"][0]["user_input"]).title(),
        "duration": results["exercises"][0]["duration_min"],
        "calories": results["exercises"][0]["nf_calories"],
    }

    return nutrition_dict



def postToSheet(data:dict) -> int:
    
    body = {
        "workout": data
    }
    headers = {
        "Authorization": os.getenv("AUTHORIZATION")
    }
    user_id = os.getenv("USER_ID")
    sheety_endpoint = f"https://api.sheety.co/{user_id}/workoutTracker/workouts"
    
    respons = requests.post(url=sheety_endpoint, json=body, headers=headers)

    return respons.status_code


if __name__ == "__main__":
    main()
