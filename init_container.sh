#!/bin/sh

set -e 

# Start Flask with Gunicorn
exec gunicorn -b 0.0.0.0:8000 app:app