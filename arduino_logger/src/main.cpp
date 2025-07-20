#include <Arduino.h>
void setup() {
Serial.begin(9600);
}

void loop() {
    while(1)
        Serial.println("Hello");
}