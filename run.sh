#!/usr/bin/env bash

# start flask
cd server
source venv/bin/activate
python app.py &
cd  ..

# start frontend
cd client
npm start 
