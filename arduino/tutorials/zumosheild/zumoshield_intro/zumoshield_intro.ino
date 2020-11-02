#include <Wire.h>
#include <ZumoShield.h>

ZumoBuzzer buzzer;
ZumoReflectanceSensorArray reflectanceSensors;
ZumoMotors motors;
Pushbutton button(ZUMO_BUTTON);

int lastError = 0;

int LINE_TRACKING = 1;
int AVOID_OBJECT = 2;
int FIND_LINE = 3;

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
  STATE = FIND_LINE;
  Serial.println("Init complete");
}

int lineTracking(int error, int distance){
  if (distance <= 10) {
    return AVOID_OBJECT;
  }
  
  if (error > 1000){
     motors.setSpeeds(200, 0);
  } else if (error < -1000){
    motors.setSpeeds(0, 200);
  }
  return LINE_TRACKING;
}

int avoidObject(){
  motors.setSpeeds(200, 0);
  delay(250);
  motors.setSpeeds(200,200);
  delay(500);
  motors.setSpeeds(0, 200);
  delay(250);
  motors.setSpeed(200, 200);
  delay(500);
  motors.setSpeed(0, 0);
  return FIND_LINE;
}

void loop() {
  unsigned int sensors[6];
  int pos = reflectanceSensors.readLine(sensors);
  int error = pos - 2500;
  if (STATE == LINE_TRACKING){
    STATE = lineTracking(error, 10);
  } else if (STATE == AVOID_OBJECT){
    STATE = avoidObject();
  } else if (STATE == FIND_LINE){
    //do whatever it is that we need to find the line
    // drive straight 
    // if line found
    // change to linetracking mode 
  }
}
