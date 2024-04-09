# MQTT project

## Mqqt basic implementation

- Info: This project is under construction

## Instructions:

- To install dependencies run: pip install -r requirements.txt
- for downloading mosquito run: docker run --name mosquitto -it -p 1883:1883 -p 9001:9001 -v ~/Projects/elevator-mqtt-monitor/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto (check the path to the file mosquitto.conf on your computer) ( this command will downloand the lastest eclipse-mosquitto version)

  or
  docker run -it -p 1883:1883 eclipse-mosquitto

to acess the shell from the mosquitto container run: sudo docker exec -it <containerId or name>

sudo apt-get update -y && sudo apt-get upgrade -y

- To install mosquitto on yout ubuntu run the comands bellow:
  sudo apt-get update -y && sudo apt-get upgrade -y  
   sudo apt-get install mosquitto
  sudo apt-get install mosquitto-clients

- Testing in terminal from the mosquito-clients: mosquitto_sub -t "test"
  mosquitto_pub -m "Mensagem" -t "test"

- To set a password to MQTT broker, run inside the container the following commad: mosquitto_passwd -c /mosquitto/config/pass <username>

- To set a virtual environment for python:
  python -m venv environment_name
  source environment_name/bin/activate
