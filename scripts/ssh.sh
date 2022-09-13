#!/bin/bash

IP=$(python aws/get_server_IP.py)

ssh -i ~/.ssh/rprater_mac.pem ec2-user@$IP