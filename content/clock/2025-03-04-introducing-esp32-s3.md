---
title:  Introducing ESP32-S3
date: 2025-03-04
---

Searching for a New Processor
=============================
I wanted to find a new [SoC][1] as a replacement for the [Assembled Adafruit Feather M0 WiFi - ATSAMD21 + ATWINC1500][2] that I used for my first try. Fortunately, I found the [Expressif ESP32][3] chip and I purchased an [ESP32­-S3­-DevKitC-1 - ESP32-S3-WROOM-2 - 32MB Flash 8MB PSRAM][4] from Adafruit.

Why It Might Work
=================
The new ESP32 chip contains a large number of peripherals which are useful for this project like:

* Sophisticated power control.
* WiFi hardware (with antenna)
* [SPI][5] bus for communicating with the e-ink display.
* [I2C][6] bus for other peripherals.

There are also a lot more functions included in the SoC so if you want to do sophisticated projects you should take a look at this. It's pretty great. Additionally, I'm a mac user and so it's great to have an environment that is quite flexible and integrates with my current tools (Visual Studio Code / Git). In comparison to [my first attempt][7] it comes with an integration level that should work a lot better that before. However, I need to test it to make sure it's do what I want.

Given that many of the features are not that unusual I'm going to focus on the trickiest problem that I had from the previous iteration, power consumption. That's what I'll tackle next.

[1]: https://en.wikipedia.org/wiki/System_on_a_chip
[2]: https://www.adafruit.com/product/2598
[3]: https://www.espressif.com/en/products/socs/esp32
[4]: https://www.adafruit.com/product/5364
[5]: https://en.wikipedia.org/wiki/Serial_Peripheral_Interface
[6]: https://en.wikipedia.org/wiki/I²C
[7]: {filename}2025-02-27-first-attempt.md