#include <Servo.h>
Servo myservo;  
int pos = 20;  
const int trigPin = 5;
const int echoPin = 6;
const int led = 13;

long duration;
float distance;

void setup() 
{
  myservo.attach(11);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT); 
  pinMode(led, OUTPUT);
  myservo.write(pos);
}

void loop() 
{
  //Serial.begin(9600);
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = 0.034*(duration/2);
  //Serial.println(distance);
  if (distance < 27)
  {
    digitalWrite(led,HIGH);
    myservo.write(pos+160);
    delay(1000);
  }
  else 
  {
    digitalWrite(led,LOW);
      myservo.write(pos);
  }
  delay(300);
}