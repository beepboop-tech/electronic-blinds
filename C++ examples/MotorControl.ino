int M1dirpin = 4;
int M1steppin = 5;
int M2dirpin = 7;
int M2steppin = 6;

void setup()
{
  pinMode(M1dirpin,OUTPUT);
  pinMode(M1steppin,OUTPUT);
  pinMode(M2dirpin,OUTPUT);
  pinMode(M2steppin,OUTPUT);
}

void loop()
{
  int j;
  
  delayMicroseconds(2);
  digitalWrite(M1dirpin,HIGH);
  digitalWrite(M2dirpin,HIGH);
  
  for(j = 0; j <= 2000; j++)
  {
    digitalWrite(M1steppin,HIGH);
    digitalWrite(M2steppin,HIGH);
    delayMicroseconds(1);
    digitalWrite(M1steppin,LOW);
    digitalWrite(M2steppin,LOW);
    delay(1);
  }
  delay(2000);
}
