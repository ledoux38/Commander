
#include <ESP8266WiFi.h>
#include <ArduinoJson.h>

// WiFi Router Login - change these to your router settings
const char* SSID = "";
const char* password = "";
const size_t CAPACITY = JSON_ARRAY_SIZE(3);

StaticJsonDocument<CAPACITY> doc;

WiFiServer WebServer(80);
WiFiClient client;

void setup() {
  Serial.begin(115200);
  delay(10);
  Serial.println();

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

  // Read the first line of the request
  String request = client.readStringUntil('\r\n');
  Serial.println(request);
  client.flush();

  // Return the response
  JsonArray array = doc.to<JsonArray>();
  array.add("hello");
  array.add(42);
  array.add(3.14);

  serializeJson(doc, client);

  delay(1);
  Serial.println("User disconnected");
  Serial.println("");

}
