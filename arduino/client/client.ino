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

#define DHT11_PIN 5

void setup()
{
  Serial.begin(115200);
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
    inByte = Serial.read();
  }
  if (inByte == 1 || 1)
  {
     String dht11 = read_dht11();
     Serial.println(dht11);
     Serial.println(inByte);
     // while(Serial.read()>0);
   }
   else
   {
   }
  
}


