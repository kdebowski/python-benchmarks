#!/bin/bash

exec gunicorn main:app -b 0.0.0.0:8080 --worker-class sanic.worker.GunicornWorker