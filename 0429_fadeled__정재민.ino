int redPin = 3;
int brightness = 0;
int fadeAmount = 1;

//코드 실행시 한번만 실행
void setup()
  // 핀 번호 2을 출력으로 선언
{
  pinMode(redPin, OUTPUT);
}

//반복구문
void loop()
{
analogWrite(redPin, brightness);
brightness = brightness + fadeAmount;

if (brightness <= 0 || brightness >= 255) {
fadeAmount = -fadeAmount;
}

delay (30);

}