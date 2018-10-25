#!/bin/bash

exec gunicorn app:run_app -b 0.0.0.0:8080 --worker-class aiohttp.GunicornWebWorker