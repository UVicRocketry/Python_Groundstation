#include <Arduino.h>
void setup() {
Serial.begin(9600);
}

void loop() {
    for ( int i = 0; i < 1000; i++) {
        Serial.println(i);
    }
}