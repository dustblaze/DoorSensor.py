const int doorPin = 4;
const int OPEN = LOW;
const int CLOSED = HIGH;
int val = LOW;
int tmp = HIGH;
int delayval = 1000;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(doorPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  tmp = digitalRead(doorPin);

  //OPEN
  if (tmp != val && tmp == OPEN) {
    val = tmp;
    //Serial.println(1);
    Serial.write(1);
  }
  //CLOSED
  else if (tmp != val && tmp == CLOSED) {
    val = tmp;
    //Serial.println(0);
    Serial.write(0);
  }
  delay(delayval);
}
