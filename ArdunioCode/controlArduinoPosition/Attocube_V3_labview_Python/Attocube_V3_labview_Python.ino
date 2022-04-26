
#include <Wire.h>
#include <Adafruit_ADS1015.h>

Adafruit_ADS1115 ads;  /* Use this for the 16-bit version */
//ADC Range: +/- 6.144V (1 bit = 3mV/ADS1015, 0.1875mV/ADS1115)



int TriggerVR1 = 53;          // Trigger VREF-1 Output Pot 1,2
int TriggerVR2 = 52;          // Trigger VREF-1 Output Pot 3,4
int Pot1 = A0;                // potentiometer wiper (middle terminal) connected to analog pin 0
int Pot2 = A1;                // potentiometer wiper (middle terminal) connected to analog pin 1
int Pot3 = A2;                // potentiometer wiper (middle terminal) connected to analog pin 2
int Pot4 = A3;                // potentiometer wiper (middle terminal) connected to analog pin 3
int val = 0;                  // variable to store the value read
int Ex_Duration = 10;         //Duration of excitation-pulse in ms (min 7 ms ?)
float Measuring_Period = 0.5;     //Delay between two excitation pulses (s)
String DataString = "";
String InputString = "";
unsigned long LastEx = 0;
int Pind, Dind, Mind;
float Pvalue, Dvalue;
String temp;
unsigned long ActTime = 0;
boolean doMeasurement = false;

void setup() {
  Serial.begin(9600);           //  setup serial
  pinMode(TriggerVR1, OUTPUT);  // sets the digital pin 53 as output
  pinMode(TriggerVR2, OUTPUT);  // sets the digital pin 52 as output

  // The ADC input range (or gain) can be changed via the following
  // functions, but be careful never to exceed VDD +0.3V max, or to
  // exceed the upper and lower limits if you adjust the input range!
  // Setting these values incorrectly may destroy your ADC!
  //                                                                ADS1015  ADS1115
  //                                                                -------  -------
  // ads.setGain(GAIN_TWOTHIRDS);  // 2/3x gain +/- 6.144V  1 bit = 3mV      0.1875mV (default)
  ads.setGain(GAIN_ONE);        // 1x gain   +/- 4.096V  1 bit = 2mV      0.125mV
  //ads.setGain(GAIN_TWO);        // 2x gain   +/- 2.048V  1 bit = 1mV      0.0625mV
  // ads.setGain(GAIN_FOUR);       // 4x gain   +/- 1.024V  1 bit = 0.5mV    0.03125mV
  // ads.setGain(GAIN_EIGHT);      // 8x gain   +/- 0.512V  1 bit = 0.25mV   0.015625mV
  // ads.setGain(GAIN_SIXTEEN);    // 16x gain  +/- 0.256V  1 bit = 0.125mV  0.0078125mV
  ads.begin();

}


void loop() {

  ActTime = millis();
   if (ActTime - LastEx > 1000 * Measuring_Period - float(Ex_Duration)||doMeasurement) {
  // if (doMeasurement) { //activate ONLY this for Python only
    doMeasurement = false;
    
    digitalWrite(TriggerVR1, 0);  // sets the Output 0  Vref1=on
    digitalWrite(TriggerVR2, 0);  // sets the Output 0  Vref2=on
    delay(Ex_Duration);

    DataString = "P1:" + String(ads.readADC_SingleEnded(0)) + "P2:" + String(ads.readADC_SingleEnded(1)) + "P3:" + String(ads.readADC_SingleEnded(2)) + "P4:" + String(ads.readADC_SingleEnded(3)) + "D:" + String(Ex_Duration) + "P:" + String(Measuring_Period);


    digitalWrite(TriggerVR1, 1);  // sets the Output 1  Vref1=off
    digitalWrite(TriggerVR2, 1);  // sets the Output 1  Vref2=off
    LastEx = millis();
  }

  if (Measuring_Period < 0.03) {
    Measuring_Period = 0.03;
  }
  if (Ex_Duration < 5) {
    Ex_Duration = 5;
  }

  if (DataString != "") {
    Serial.println(DataString);
    //Serial.println("     "+ String(Measuring_Period)+"  Ex_duration: "+String(Ex_Duration));
    DataString = "";
  }

  if (Serial.available()) {

    InputString = Serial.readString();

    if (InputString.indexOf('P') || InputString.indexOf('D') || InputString.indexOf('M') ){
      Pind = InputString.indexOf('P');
      Dind = InputString.indexOf('D');
      Mind = InputString.indexOf('M');
      if (Pind > Dind) {
        temp = InputString.substring(Pind + 1);
        Measuring_Period = temp.toFloat();
      }
      else {
        temp = InputString.substring(Dind + 1);
        Ex_Duration = temp.toFloat();
      }

    }
    if (Pind > -1 && Dind > -1) {
      if (Pind > Dind) {
        temp = InputString.substring(Dind + 1, Pind);

        Ex_Duration = temp.toFloat();
      }
      else {
        temp = InputString.substring(Pind + 1, Dind);
        Measuring_Period = temp.toFloat();

      }
    }
    if (Mind > -1 ){
      doMeasurement = true;
    }

  }
}









//val = analogRead(Pot1);       // read the input pin
//Serial.println(val);          // debug value
//val = analogRead(Pot2);       // read the input pin
//Serial.println(val);          // debug value
//val = analogRead(Pot3);       // read the input pin
//Serial.println(val);          // debug value
//val = analogRead(Pot4);       // read the input pin
//Serial.println(val);          // debug value
//Serial.println();
//
//digitalWrite(TriggerVR1, 1);  // sets the Output 1  Vref1=off
//digitalWrite(TriggerVR2, 1);  // sets the Output 1  Vref2=off
//delay(1000);
