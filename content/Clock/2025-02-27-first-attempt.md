---
title:  First Attempt
date: 2025-02-24
category: Clock
---

What Did I Do?
==============
I finished the first attempt at my clock using an [Assembled Adafruit Feather M0 WiFi - ATSAMD21 + ATWINC1500][1] as the CPU/WiFi/RTC and an [Adafruit 24LC32 I2C EEPROM Breakout - 32Kbit / 4 KB - Stemma QT][2] as the EEPROM. The idea was to keep the parameters that need to be stored between power cycles in the EEPROM. The "completed" project is shown below.

![First Clock Attempt][3]

What Went Right?
================
The project worked. It kept track of time and used the WiFi to update the time on a regular basis. One pleasant surprise was that the drift was low so I only needed to do sub-one second corrections once a week. The e-ink display worked well but early on I figured that the flashing nature of the display precluded it from being used in an area like a living room where the flash would be noticeble and draw your attention. However, it will suit its original purpose well.

What Went Wrong?
================
The big one was power consumption. The WiFi module is coupled to the rest of the system and it did not respond well to being shut down. Also, the Arduino development environment doesn't (IMO) work well because you have to carry around a lot of extra stuff and that gets in the way of doing what I want. The environment makes is a breeze to do quite a few things but if you need a lot of control it's not really that great. This showed me some pain points that I need to pay attention to:

* Low power. Since this is a clock that hangs on the wall it should last a minimum of three months on a battery. The longer the better.
* Robust WiFi hardware. My first attempt has really good WiFi but I'd like something that can be enabled/disabled at a whim.
* Driver for the e-ink display. The drivers supplied were good but they were Arduino dependent. I'd like something a little more useable.

My Partial Second Attempt
=========================
I wanted to use some hardware from SparkFun's smôl series so I purchased some CPU boards and some other pieces of hardware just in time for them to completely bail on the entire line. Not cool SparkFun. I now have some unsupported hardware that I cannot do that much with. It's really too bad since the architecture was quite interesting in that the main focus was low power and small size.


[1]: https://www.adafruit.com/product/2598
[2]: https://www.adafruit.com/product/5146
[3]: {attach}images/first_clock_attempt.jpg
