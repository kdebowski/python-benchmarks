#!/bin/bash

exec gunicorn main:run_app -b 0.0.0.0:8080 --worker-class aiohttp.GunicornWebWorker