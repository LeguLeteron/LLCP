void setup()
{

  Serial.begin(9600);  // initialize serial communications at 9600 bps

}

void loop()
{
//  char *readString = "";
//  while(!Serial.available()) {}
//  // serial read section
//  while (Serial.available())
//  {
//    Serial.print(Serial.read());
//    if (Serial.available()>0)
//    {
//      char c = Serial.read();  //gets one byte from serial buffer
//      readString += c; //makes the string readString
//    }
//  }
//
//  if (sizeof(readString) >0)
//  {
//    Serial.print("Arduino received: ");  
//    Serial.println(readString); //see what was received
//  }
//
//  delay(500);
//
//  // serial write section

  Serial.write(8);
  Serial.flush();
}
