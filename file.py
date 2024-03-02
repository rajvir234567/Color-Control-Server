# include <WiFi.h>
# include <WiFiClient.h>
# include <WebServer.h>
# include <ESPmDMS.h>

const char* ssid = "VM8751745"
const char* password = "smnwrmMxq4sd"

string button = "<html>
                 <body id='bdy_1"
style ='height:100px;
width:100px'>

webServer server(80); // http port number

void handleRoot(){
 //(192.168.1.1.){
  server.send(200, "text/html", button); // here 200 is a success code   
 } 
}
void handleNotFound(){
    string message = "File Not Found \n\n";
    message += "URL:"; //(192.168.1.1)
    message += server.url();
    message += "\n Method"
    message += "\n"   
}

const int led_1 =2;
const int buzzer =15;

pinMode(LED_1, OUTPUT);
pinMode(BUZZER, OUTPUT);

Serial.begin(115200);