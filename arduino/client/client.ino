//
// FILE: monit client
// AUTHOR: Yuanbo
// VERSION: 0.1
//
#include "dht.h"

//
dht DHT;
//

String inByte;

#define CMD_READ "read"
#define CMD_WRITE "write"


#define LED_PIN   13
#define DHT11_PIN 5

void setup()
{
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  while(Serial.read()>0);
}

// dht11
String read_dht11(void)
{
  String t = "dht11;";
  int chk;
  int mtry = 0;
  while(((chk=DHT.read11(DHT11_PIN)) != DHTLIB_OK)&&mtry<1000)
  {
    delay(100);
    mtry++;
  }
  if(mtry>=1000)
  {
    t="dht11;ERROR;";
  }
  else
  {
    t = t + "OK;";
    t = t + "humidity=" + DHT.humidity + "&&";
    t = t + "temperature=" + DHT.temperature ;
  }
  return t;
}

void loop()
{
  if (Serial.available() > 0)
  {
    inByte = Serial.readString();
    delay(1000);
  }
  if (!inByte.compareTo(CMD_READ))
  {
     String dht11 = read_dht11();
     Serial.println(dht11);
     Serial.println(inByte);
     inByte = "";
   }
   else if (!inByte.compareTo("write0"))
   {
     digitalWrite(LED_PIN, LOW);
   }
   else if(!inByte.compareTo("write1"))
   {
     digitalWrite(LED_PIN, HIGH);
   }
     delay(1000);
  
}


