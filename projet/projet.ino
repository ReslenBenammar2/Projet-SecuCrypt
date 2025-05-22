#include <math.h>

int ledPin = 12;  
int analogPin = A0; 
int Soff, Son;      

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(ledPin, HIGH);
  delay(1000); 
  Son = analogRead(analogPin); 

  digitalWrite(ledPin, LOW);
  delay(1000); 
  Soff = analogRead(analogPin); 

  
  float A = -log10((float)Son / (float)Soff);

  Serial.print("Soff = ");
  Serial.print(Soff);
  Serial.print(" | Son = ");
  Serial.print(Son);
  Serial.print(" | Absorbance = ");
  Serial.println(A, 4); 
}
