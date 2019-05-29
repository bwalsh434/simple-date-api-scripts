#!/bin/bash
sudo yum install unzip -y
sudo yum install python36 -y
sudo yum install python36-pip -y

artifact=$(gsutil ls gs://simple-date-api-artifacts | sort -V | tail -n1 | xargs basename)
sudo gsutil cp gs://simple-date-api-artifacts/$artifact .
sudo unzip -o $artifact
sudo rm -rf /opt/simple-date-api
sudo mv -f simple-date-api /opt/
sudo pip3 install -r /opt/simple-date-api/requirements.txt
sudo python3 /opt/simple-date-api/simple-date-api/app.py

