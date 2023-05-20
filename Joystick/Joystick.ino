// Pin numbers for each measurement
const int analogBottom = A1;
const int analogTopX = A2;
const int analogTopY = A3;
const int topButton = A4;

void setup()
{
    // Set up the digital pins to be in input mode,
    // and set up the baud rate of the
    pinMode(topButton, INPUT);
    Serial.begin(115200);
}

void loop()
{
    // Send all variables through serial, delimited using commas,
    // every 50 milliseconds
    Serial.print(analogRead(analogBottom));
    Serial.print(",");
    Serial.print(digitalRead(topButton));
    Serial.print(",");
    Serial.print(1023-analogRead(analogTopY));
    Serial.print(",");
    Serial.println(analogRead(analogTopX));
    delay(50);
}
