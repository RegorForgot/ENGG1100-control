// Pin numbers for each measurement
const int topButton = 8;
const int analogBottom = 3;
const int analogTopY = 1;
const int analogTopX = 0;

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
    Serial.print(analogRead(analogTopY));
    Serial.print(",");
    Serial.println(1023 - analogRead(analogTopX));
    delay(50);
}
