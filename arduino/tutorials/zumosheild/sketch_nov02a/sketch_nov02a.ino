#include <Wire.h>
#include <ZumoShield.h>

ZumoBuzzer buzzer;
ZumoReflectanceSensorArray reflectanceSensors;
ZumoMotors motors;
Pushbutton button(ZUMO_BUTTON);

int lastError = 0;

int LINE_TRACKING = 1;

int STATE;

void init_robot() {
  buzzer.play(">g32>>c32");
  reflectanceSensors.init();
  button.waitForButton();
  delay(1000);
  int i;
  for (i = 0; i < 80; i++)
  {
    if ((i > 10 && i <= 30) || (i > 50 && i <= 70))
      motors.setSpeeds(-200, 200);
    else
      motors.setSpeeds(200, -200);
    reflectanceSensors.calibrate();

    // Since our counter runs to 80, the total delay will be
    // 80*20 = 1600 ms.
    delay(20);

  }
  motors.setSpeeds(0, 0);
  buzzer.play(">g32>>c32");
  button.waitForButton();
//  buzzer.play("L16 cdegreg4");
//  while (buzzer.isPlaying());
}

void setup() {
  Serial.begin(115200);
  Serial.println("init cool robot thing");
  init_robot();
  STATE = LINE_TRACKING;
  Serial.println("Init complete");
}

int lineTracking(int error){
  if (error > 1000){
     motors.setSpeeds(200, 0);
  } else if (error < -1000){
    motors.setSpeeds(0, 200);
  }
  return LINE_TRACKING;
}

void loop() {
  unsigned int sensors[6];
  int pos = reflectanceSensors.readLine(sensors);
  int error = pos - 2500;
  if (STATE == LINE_TRACKING){
    STATE = lineTracking(error);
  }
}
