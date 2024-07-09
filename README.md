# IvyBot Assembly and Programming Guide

## Overview

The IvyBot is a modular robot made up of several components, including an IvyBot Body, an IvyBot Bottom, servo holders, and a Circuit Playground Express with the Adafruit CRICKIT for Circuit Playground Express.

### Components

- **IvyBot Bottom w/ Servo Holder**
  - **Description**: The bottom assembly of the IvyBot, which includes the IvyBot Bottom panel and four servo holders.
  - **SolidWorks Assembly File**: `IvyBot Bottom with holder.SLDPRT.SLDASM`
  - **STL Files for Complete Assembly**: 
    - `IvyBot Bottom with holder - IvyBot Bottom-1.STL`
    - `IvyBot Bottom with holder - Servo Holder-2.STL`
    - `IvyBot Bottom with holder - Servo Holder-4.STL`
    - `IvyBot Bottom with holder - Servo Holder-5.STL`
    - `IvyBot Bottom with holder - Servo Holder-6.STL`
  
  - **IvyBot Bottom**
    - **Description**: The panel that forms the base of the IvyBot's bottom assembly.
    - **SolidWorks File**: `IvyBot Bottom.SLDPRT`
    - **STL File**: `IvyBot Bottom.STL`
  
  - **Servo Holder**
    - **Description**: Holders designed to mount servos securely to the IvyBot Bottom. Four servo holders are used in this assembly.
    - **SolidWorks File**: `Servo Holder.SLDPRT`
    - **STL File**: `Servo Holder.STL`

The `IvyBot Bottom with holder.SLDPRT.SLDASM` assembly file provides a complete assembled view of the IvyBot Bottom with the Servo Holders.

The STL files listed below should be imported all together into the slicer to ensure they are printed correctly in their assembled positions:
- `IvyBot Bottom with holder - IvyBot Bottom-1.STL`
- `IvyBot Bottom with holder - Servo Holder-2.STL`
- `IvyBot Bottom with holder - Servo Holder-4.STL`
- `IvyBot Bottom with holder - Servo Holder-5.STL`
- `IvyBot Bottom with holder - Servo Holder-6.STL`

Importing all the STL files together into the slicer will ensure that the parts are printed in their correct relative positions, ensuring proper assembly and fit.

### Electronics

- **Circuit Playground Express**
  - [Product Link](https://www.adafruit.com/product/3333)
  - [Overview](https://learn.adafruit.com/adafruit-circuit-playground-express/overview)

- **Adafruit CRICKIT for Circuit Playground Express**
  - [Product Link](https://www.adafruit.com/product/3093)
  - [Overview](https://learn.adafruit.com/adafruit-crickit-creative-robotic-interactive-construction-kit/overview)

- **3 x AA Battery Holder with 2.1mm Plug**
  - [Product Link](https://www.adafruit.com/product/3842)

## Folder Structure

- `Code`
- `Model`
  - `Body`
    - `IvyBot Body.STL`
    - `IvyBot Body.SLDPRT`
  - `Bottom`
    - `SolidWorks`
      - `Assembly`
      - `Individual`
    - `STL`
      - `IvyBot Bottom with holder - IvyBot Bottom-1.STL`
      - `IvyBot Bottom with holder - Servo Holder-2.STL`
      - `IvyBot Bottom with holder - Servo Holder-4.STL`
      - `IvyBot Bottom with holder - Servo Holder-5.STL`
      - `IvyBot Bottom with holder - Servo Holder-6.STL`

- `Release`

## Assembly Instructions

1. **Prepare the Circuit Playground Express & Adafruit CRICKIT for Circuit Playground Express**
   - Connect them using screws, ensuring a secure connection.
2. **Print Body & Bottom**
   - Print the IvyBot Body and Bottom using the provided STL files.
3. **Assemble the Servo Holders**
   - Insert the servos into the servo holders.
4. **Connect the Servos to CRICKIT**
   - Connect the servos to the CRICKIT servo ports as indicated on the bottom.
5. **Programming**
   - Program the IvyBot using MakeCode.

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
