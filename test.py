import json
import mimetypes

import requests


def generate_presentation(prompt, presentation_time, theme_color):
    url = "http://127.0.0.1:8000/generate_presentation"
    user_input = prompt + f". The presentation time is {presentation_time}"
    user_data = {"user_input": user_input, "theme_color": theme_color}
    response = requests.post(url, data=user_data)
    response_json = response.json()
    text_json = json.loads(response_json.get('text', '{}'))
    return text_json.get('links', {}).get('web', 'No link found')


print(generate_presentation("presentation about tsunamis", "10 minutes", "white"))
