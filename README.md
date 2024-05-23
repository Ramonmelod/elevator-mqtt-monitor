# MQTT project

<div>
<img src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="logo python" width="200" height="auto"> 
<img src="https://repository-images.githubusercontent.com/53614190/b11dd480-90b3-11eb-903d-8c48f62e3172" alt="logo mosquitto" width="200" height="auto">
</div>

## Used Technologies:

- `Eclipse-Mosquitto MQTT broker`
- `Python`

## Autor

- Ramon Melo — Linkedin: [/in/ramonmelod](https://www.linkedin.com/in/ramonmelod/)

## Mqqt basic implementation

- Info: This project is under construction and compose.yml is not ready yet

## Instructions:

### Installing dependencies and running MQTT broker on docker

- To install dependencies run: pip install -r requirements.txt
- Before running moquitto on docker erase: `password_file /mosquitto/config/pass` from the file mosquitto.conf then run the comand bellow mapping the path for your file mosquitto.config on your computer.

- for downloading mosquito run: docker run --name mosquitto -it -p 1883:1883 -p 9001:9001 -v ~/Projects/elevator-mqtt-monitor/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto (check the path to the file mosquitto.conf on your computer) ( this command will downloand the lastest eclipse-mosquitto version)

- After running mosquitto on docker access the shell from the mosquitto container by the command: sudo docker exec -it <containerId or name>
- Inside your container run the following commad for defining a User and a Password: mosquitto_passwd -c /mosquitto/config/pass <username>
- Stop the conainer and rewrite inside the file mosquitto.conf: `password_file /mosquitto/config/pass`

### installing Mosquitto broker on your ubuntu

- After running: sudo apt-get update -y && sudo apt-get upgrade -y

run the comands bellow:
sudo apt-get update -y && sudo apt-get upgrade -y  
 sudo apt-get install mosquitto
sudo apt-get install mosquitto-clients

- After the instalation of the mosquito and mosquitto-clients on your ubuntu you can test your broker running on the docker container by running the comands bellow:
- mosquitto_sub -t "test"
- mosquitto_pub -m "Mensagem" -t "test"

### Setting a virtual environment for python:

- To set a virtual environment for python:
  python -m venv environment_name

  source environment_name/bin/activate

### Using a Esp32 to monitor a sign

- the file esp32publisher.py shell be used as code for micropython on a esp32
- this project uses the uses: ESP32_GENERIC-20240222-v1.22.2. You can try other version of micropython, but risks of unexpected behavior are always possible
