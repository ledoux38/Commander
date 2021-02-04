
#include <ESP8266WiFi.h>
#include <ArduinoJson.h>

// WiFi Router Login - change these to your router settings
const char* SSID = "Livebox-B6DE";
const char* password = "vJKCMEXyJmmmDNpDJC";

const size_t CAPACITY = JSON_ARRAY_SIZE(3);
StaticJsonDocument<CAPACITY> doc;

// Create the ESP Web Server on port 80
WiFiServer WebServer(80);
// Web Client
WiFiClient client;

// INPUT - OUTPUT
int GPIO1 = 5;
int GPIO2 = 4;
int GPIO3 = 0;
int GPIO4 = 2;

int GPIO5 = 16;
int GPIO6 = 14;
int GPIO7 = 12;
int GPIO8 = 13;

void setup() {
  Serial.begin(9600);
  
  pinMode(GPIO1, OUTPUT); 
  pinMode(GPIO2, OUTPUT); 
  pinMode(GPIO3, OUTPUT); 
  pinMode(GPIO4, OUTPUT);
   
  pinMode(GPIO5, INPUT); 
  pinMode(GPIO6, INPUT); 
  pinMode(GPIO7, INPUT); 
  pinMode(GPIO8, INPUT); 
  
  delay(10);


  // Connect to WiFi network
  Serial.println();
  WiFi.disconnect();
  WiFi.mode(WIFI_STA);
  Serial.print("Connecting to ");
  Serial.println(SSID);
  WiFi.begin(SSID, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("Connected to WiFi");

  // Start the Web Server
  WebServer.begin();
  Serial.println("Web Server started");

  // Print the IP address
  Serial.print("You can connect to the ESP8266 at this URL: ");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/");
}

void loop() {
  // Check if a user has connected
  client = WebServer.available();
  if (!client) {//restart loop
    return;
  }

  // Wait until the user sends some data
  Serial.println("New User");
  while (!client.available()) {
    delay(1);
  }

  // Return the response
  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: application/json");
  client.println("");

  StaticJsonDocument<200> doc;
  
  JsonArray input = doc.createNestedArray("input");
  input.add(digitalRead(GPIO1));
  input.add(digitalRead(GPIO2));
  input.add(digitalRead(GPIO3));
  input.add(digitalRead(GPIO4));

  JsonArray output = doc.createNestedArray("output");
  output.add(digitalRead(GPIO5));
  output.add(digitalRead(GPIO6));
  output.add(digitalRead(GPIO7));
  output.add(digitalRead(GPIO8));
  
  serializeJson(doc, client);
  
  delay(1);
  Serial.println("User disconnected");
  Serial.println("");

}
