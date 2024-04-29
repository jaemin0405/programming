int greenPin = 2;
int redPin = 13;
int yellowPin = 10;


// 코드는 실행시 한번만 실행된다.
// 세팅하는 곳
void setup()
{
  pinMode(greenPin, OUTPUT);
  pinMode(redPin, OUTPUT);
  pinMode(yellowPin, OUTPUT);
  
}

//반복하여 일을 실행 시키는 곳
void loop()
{
  //led를 켠다
  digitalWrite(greenPin, HIGH);
  //출력해라. greenPin을 HIGH로 출력하라
  delay(1000); // 1초 기다리기
  //led를 끈다
  digitalWrite(greenPin, LOW); //출력해라. greenPin을 LOW로 출력하라
  delay(1000); // 1초 기다리기
  
  //빨강 led
  digitalWrite(redPin, HIGH);
  delay(1000); //1초 기다리기
  
  digitalWrite(redPin, LOW);
  delay(1000); //1초 기다리기
  
  //노랑 led
  digitalWrite(yellowPin, HIGH);
  delay(1000); //1초 기다리기
  
  digitalWrite(yellowPin, LOW);
  delay(1000); //1초 기다리기
  
  
  
  
  
}