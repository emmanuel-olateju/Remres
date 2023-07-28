int EMGPin = A1;
int EMGVal = 0;
int emg=0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  if(Serial.available()>0){
    emg = Serial.read();
    EMGVal = analogRead(EMGPin);
    Serial.write(EMGVal & 0xff);
    Serial.write(EMGVal>>8);
    Serial.write('\n');
  }
}