int EMGPin = A1;
int EMGVal = 0;
int emg=0;

void setup() {
  Serial.begin(2000000);
}

void loop() {
  Serial.flush();
  if(Serial.available()>0){
    emg=Serial.read();
    EMGVal = analogRead(EMGPin);
    Serial.write(EMGVal & 0xff);
    Serial.flush();
    Serial.write(EMGVal>>8);
    Serial.flush();
    Serial.write('\n'); 
    Serial.flush(); 
  }
//    EMGVal = analogRead(EMGPin);
//    Serial.write(EMGVal & 0xff);
//    Serial.flush();
//    Serial.write(EMGVal>>8);
//    Serial.flush();
//    Serial.write('\n'); 
//    Serial.flush();
}
