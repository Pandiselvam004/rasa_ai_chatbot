from flask_socketio import SocketIO, emit
from flask_cors import CORS
from flask import Flask, jsonify
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
cors = CORS(app)

@socketio.on('connect')
def test_connect():
    print('Client connected')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('user_uttered')
def handle_message(message):
    # Process the user's message
    # ...
    # Send the bot's response to the client
    emit('bot_uttered', {'text': 'Hello, World!'})

class ActionWeather(Action):
    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.latest_message['entities'][0]['value']
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"

        response = requests.get(url).json()

        weather_description = response['weather'][0]['description']
        temperature = response['main']['temp']
        humidity = response['main']['humidity']

        message = f"The weather in {city} is {weather_description}, with a temperature of {temperature} Kelvin and a humidity of {humidity}%."

        dispatcher.utter_message(text=message)

        return []
    
class ActionOrderStatus(Action):
    def name(self) -> Text:
        return "action_order_status"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        order_id = tracker.latest_message['entities'][0]['value']

        message = f"Make a functional process for this order id : {order_id}"

        dispatcher.utter_message(text=message)

        return []
