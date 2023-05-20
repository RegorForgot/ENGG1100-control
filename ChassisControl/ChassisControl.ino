#include <ESP8266WiFi.h>
#include <Servo.h>
#include <WebSocketServer.h>

Servo pan, tilt;
const int motorBack = 5;
const int motorForward = 4;
const int pump = 14;
const int deadzone = 32;
const int maxJoystick = 1024;
const double servoSensitivity = 0.049;
int currentPan = 1400;
int currentTilt = 1400;

String data;
String *separatedData;
int *parsedData;

WiFiServer server(80);
WebSocketServer webSocketServer;

void setup()
{
    const char *ssid = "ENGG1100-YellowCII";

    // Attaching GPIO pins to servo functionality.
    pinMode(pump, OUTPUT);
    pinMode(motorBack, OUTPUT);
    pinMode(motorForward, OUTPUT);

    // Servo control pin and range as calibrated
    pan.attach(12);
    tilt.attach(13);

    // Setting up serial and PWM range/frequency
    Serial.begin(115200);
    analogWriteRange((maxJoystick - deadzone) / 2);
    analogWriteFreq(40000);

    // Setting up access-point WiFi connection
    Serial.println("Setting soft-AP configuration ... ");
    WiFi.softAP(ssid);
    Serial.println(WiFi.softAPIP());
    Serial.println(WiFi.SSID());

    server.begin();
}

int *receivedParse(String &data)
{
    // Method to take data given via websocket and turn it into 4 integers
    // required for controlling different parts of system.
    separatedData = new String[4];
    parsedData = new int[4];
    int substringCount;

    while (data.length() > 0)
    {
        int index = data.indexOf(',');
        if (index == -1) // No commas found
        {
            separatedData[substringCount++] = data;
            break;
        }
        else
        {
            separatedData[substringCount++] = data.substring(0, index);
            data = data.substring(index + 1);
        }
    }

    // Converting the strings into integers and then freeing memory allocations
    for (int i = 0; i < 4; i++)
    {
        parsedData[i] = atoi(separatedData[i].c_str());
    }
    delete[] separatedData;
    return parsedData;
}

void moveBidirectional(int input, int &currentVal, Servo &servo, bool tilt)
{
    if (input < (maxJoystick - deadzone) / 2)
    {
        // Checks if servo amount is over the maximum allowed value
        if (currentVal < 2140)
        {
            currentVal += (int)floor(((maxJoystick - deadzone) / 2 - input) * servoSensitivity);
            servo.writeMicroseconds(currentVal);
        }
    }
    else if (input > (maxJoystick + deadzone) / 2)
    {
        if ((580 < currentVal) & tilt | (520 < currentVal) & !tilt)
        {
            currentVal -= (int)floor((input - (maxJoystick + deadzone) / 2) * servoSensitivity);
            servo.writeMicroseconds(currentVal);
        }
    }
}

void loop()
{
    // Getting any connected networks
    WiFiClient controller = server.available();
    if (controller.connected() && webSocketServer.handshake(controller))
    {
        while (controller.connected())
        {
            data = webSocketServer.getData();
            if (data.length() > 0)
            {
                Serial.println(data);
                parsedData = receivedParse(data);
                digitalWrite(pump, parsedData[1]);

                if (parsedData[0] < (maxJoystick - deadzone) / 2)
                {
                    analogWrite(motorBack, ((maxJoystick - deadzone) / 2) - parsedData[0]);
                    analogWrite(motorForward, 0);
                }
                else if (parsedData[0] > (maxJoystick + deadzone) / 2)
                {
                    analogWrite(motorForward, parsedData[0] - (maxJoystick + deadzone) / 2);
                    analogWrite(motorBack, 0);
                }
                else
                {
                    analogWrite(motorBack, 0);
                    analogWrite(motorForward, 0);
                }
                moveBidirectional(parsedData[2], currentTilt, tilt, true);
                moveBidirectional(parsedData[3], currentPan, pan, false);
                delete[] parsedData;
            }
            delay(10); // Delay needed for receiving the data correctly
        }

        Serial.println("The controller has been disconnected!");
    }

    delay(20);
}