#!/bin/bash

NEWLINE=$'\n'

IP=$(python aws/get_server_IP.py)

CONFIG="Host ${IP}${NEWLINE}  HostName ${IP}${NEWLINE}  IdentityFile ~/.ssh/rprater_mac.pem${NEWLINE}  User ec2-user"

echo "$CONFIG" >> "/Users/robertprater/.ssh/config"