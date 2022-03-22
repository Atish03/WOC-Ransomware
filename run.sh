#!/bin/bash
python -m http.server & cloudflare/Linux/cloudflared tunnel --url http://localhost:8000 && fg
