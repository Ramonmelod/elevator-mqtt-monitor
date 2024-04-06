# MQTT project

## Mqqt basic implementation

- Info: This project is under construction

## Instructions:

- To install dependencies run: pip install -r requirements.txt
- for downloading mosquito run: docker run -it -p 1883:1883 -p 9001:9001 -v mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto
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