#!/bin/bash

IP=$(python aws/get_server_IP.py)

open "http://${IP}:8080"