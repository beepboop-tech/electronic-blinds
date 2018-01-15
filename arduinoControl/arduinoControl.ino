int upPin = 1; //initialise blinds to go up on pin 1
int downPin = 2; //initialise blinds to go down on pin 2
int receivedPin = 3; //pin to send received signal back to pi
int M1dirpin = 4; //set motor 1 direction pin
int M1steppin = 5; //set motor 1 stepping pin
int M2dirpin = 7; //set motor 2 direction pin
int M2steppin = 6; //set motor 2 stepping pin
bool receivedState = false; //variable to store the read state of the received pin

void setup() {
    pinMode(upPin, INPUT);
    pinMode(downPin, INPUT);
    pinMode(receivedPin, OUTPUT);    
    pinMode(M1dirpin,OUTPUT);
    pinMode(M1steppin,OUTPUT);
    pinMode(M2dirpin,OUTPUT);
    pinMode(M2steppin,OUTPUT);    
}

void loop() {    
  if(digitalRead(upPin) == 1){
          toggleReceivePin();
          delayMicroseconds(2);
          digitalWrite(M1dirpin,HIGH);
          digitalWrite(M2dirpin,HIGH);
          runMotor();
                  
  }else if(digitalRead(downPin) == 1){
          toggleReceivePin();
          delayMicroseconds(2);
          digitalWrite(M1dirpin,LOW);
          digitalWrite(M2dirpin,LOW);
          runMotor();                 
}        

bool toggleReceivePin(){
  digitalWrite(receivedPin, !receivedState)
  receivedState = !receivedState  
}

void runMotor(){  
  for(int j = 0; j <= 2000; j++) {
    digitalWrite(M1steppin,LOW);
    digitalWrite(M2steppin,LOW);
    delayMicroseconds(2);
    digitalWrite(M1steppin,HIGH);
    digitalWrite(M2steppin,HIGH);
    delay(1);  
  }
}
