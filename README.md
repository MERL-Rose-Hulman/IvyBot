# IvyBot Assembly and Programming Guide

## Overview

The IvyBot is a modular robot made up of several components, including an IvyBot Body, an IvyBot Bottom, servo holders, and a Circuit Playground Express with the Adafruit CRICKIT for Circuit Playground Express.

### Components

- **IvyBot Body**
  - **Description**: The main body of the IvyBot.
  - **File**: `IvyBot Body.SLDPRT`

- **IvyBot Bottom**
  - **Description**: The bottom assembly of the IvyBot, which includes the IvyBot Bottom panel and four servo holders.
  - **File**: `IvyBot Bottom.SLDPRT`
  - **STL File**: `IvyBot Bottom with holder - IvyBot Bottom-1.STL`

- **Servo Holder**
  - **Description**: Holders designed to mount servos securely to the IvyBot Bottom. Four servo holders are used in this assembly.
  - **File**: `Servo Holder.SLDPRT`
  - **STL Files**:
    - `IvyBot Bottom with holder - Servo Holder-2.STL`
    - `IvyBot Bottom with holder - Servo Holder-4.STL`
    - `IvyBot Bottom with holder - Servo Holder-5.STL`
    - `IvyBot Bottom with holder - Servo Holder-6.STL`

### Electronics

- **Circuit Playground Express**
  - [Product Link](https://www.adafruit.com/product/3333)
  - [Overview](https://learn.adafruit.com/adafruit-circuit-playground-express/overview)

- **Adafruit CRICKIT for Circuit Playground Express**
  - [Product Link](https://www.adafruit.com/product/3093)
  - [Overview](https://learn.adafruit.com/adafruit-crickit-creative-robotic-interactive-construction-kit/overview)

## Folder Structure

- `STL/`
  - `IvyBot Bottom with holder - IvyBot Bottom-1.STL`
  - `IvyBot Bottom with holder - Servo Holder-2.STL`
  - `IvyBot Bottom with holder - Servo Holder-4.STL`
  - `IvyBot Bottom with holder - Servo Holder-5.STL`
  - `IvyBot Bottom with holder - Servo Holder-6.STL`
  
- `SolidWorks/`
  - `IvyBot Bottom with holder.SLDPRT`
  - `IvyBot Bottom.SLDPRT`
  - `Servo Holder.SLDPRT`
  - `IvyBot Body.SLDPRT`

## Assembly Instructions

1. **Prepare the IvyBot Body**: Print the IvyBot Body using the STL file provided.
2. **Prepare the IvyBot Bottom**: Print the IvyBot Bottom using the STL file `IvyBot Bottom with holder - IvyBot Bottom-1.STL`.
3. **Prepare the Servo Holders**: Print four Servo Holders using the STL files provided.
4. **Assemble the Servo Holders to the IvyBot Bottom**: Attach the four Servo Holders to the IvyBot Bottom panel as per the design in the SolidWorks assembly file `IvyBot Bottom with holder.SLDPRT`.
5. **Combine the IvyBot Body and Bottom**: Attach the IvyBot Body to the assembled IvyBot Bottom.
6. **Mount the Electronics**: Install the Circuit Playground Express and Adafruit CRICKIT on the IvyBot Body as per the product guidelines.

## Programming the IvyBot

The IvyBot can be programmed using [MakeCode](https://makecode.adafruit.com/). Below is an example code that makes the IvyBot move when it's dark and stop when it's not.

### Example Code

```javascript
input.onLightConditionChanged(LightCondition.Dark, function () {
    music.powerUp.play()
})
music.playMelody("B A G A G F A C5 ", 300)
crickit.servo1.setAngle(90)
crickit.servo2.setAngle(90)
crickit.servo3.setAngle(90)
crickit.servo4.setAngle(90)
pause(1000)
forever(function () {
    if (input.lightLevel() < 30) {
        crickit.servo4.setAngle(160)
        crickit.servo2.setAngle(20)
        crickit.servo1.setAngle(20)
        crickit.servo3.setAngle(160)
        light.showAnimation(light.runningLightsAnimation, 200)
        crickit.servo4.setAngle(20)
        crickit.servo2.setAngle(160)
        crickit.servo1.setAngle(160)
        crickit.servo3.setAngle(20)
        light.showAnimation(light.runningLightsAnimation, 200)
    } else {
        light.showAnimation(light.sparkleAnimation, 500)
    }
})
