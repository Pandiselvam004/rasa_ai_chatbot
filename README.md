# Rasa AI with Custom Actions and Chat Widget
---
* Required Python version is Python 3.9.10
---
#### Local Setup Guide
* python3 -m venv venv
* source venv/bin/activate
* pip3 install -r requirements.txt
* python3 -m rasa train
* python3 -m rasa run -m models --enable-api --cors "*"
* rasa run actions --port 5055 (this one need to be run an another terminal)
* open chat.html for view widget
