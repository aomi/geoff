# Independent Directed Study - Grade 12
Aomi Jokoji & Austin Smith
![](http://i.imgur.com/vlExxYX.jpg)
_Working Final Prototype_

## Summary
We designed a shallow water monitoring vessel to measure water pH, water temperature, air temperature, humidity, and air pressure. 

![](http://i.imgur.com/bIweJNp.jpg)
_Before putting vessel in water._

The hull of the vessel was a 4ft wide inner tube between two pieces of plywood pulled together by steel rods. The brain of the vessel was a Raspberry Pi. 

![](http://i.imgur.com/n5OBnnE.jpg)
_Raspberry Pi 2 with Adafruit Motor HAT and Voltage Regulators within tuparware._

A car battery powered all electronics on the boat after going through a series of voltage regulators. 

![](http://i.imgur.com/zq4VquC.jpg)
_Car battery powering all electronics on vessel._

The water sensors were sent underwater via a probe powered by Arduino and the entire probe was moved via a winch system. The air sensors were all managed by a singular circuit on the vessel. Both sensors ran on a form of communication called I2C which allows more a modular design so more sensors could be easily added.

![](http://i.imgur.com/a2EtMjG.jpg)
_pH sensor assembly before being glued together._

The vessel was moved by a canoe trolling motor which was controlled by two relays. This gave us the ability to move forwards, backwards, and alter the speed. It was turned by a stepper motor and we 3D-printed a gear system to connect the stepper motor to the trolling motor’s shaft. 

![](http://i.imgur.com/E2AmUVc.jpg)
_Trolling motor assembly with stepper motor with 3D printed gears for steering._

The Raspberry Pi emitted a wi-fi access point which was connected to via a computer. We utilized a user interface to control the vessel’s movement as well as taking data readings every 30 seconds.

## Running the Program
This program was written to be executed on the Raspberry Pi 2 with a [Adafruit Motor HAT](https://www.adafruit.com/product/2348). This program also assumes that a way to SSH into the system has been configured. For our testing, a WiFi hotspot was made on the Raspberry Pi. This was put together for a prototype and the code and setup reflects this. 

- Clone onto Raspberry Pi
- Install requirements via pip.
```
pip install -r requirements.txt
```
- Execute program
```
python run.py
```

