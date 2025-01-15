---
layout: post
title:  "Single Multisegment Display"
date:   2015-05-24 17:33
permalink: /:categories/:title
categories: project pinball
header-img: img/project/pinball/bg/singledigit.jpg
---

Wiring up the MAX6954
=====================

I discovered the [MAX6954 4-Wire Interfaced, 2.7V to 5.5V LED Display Driver
with I/O  Expander and Key Scan][1] which I'll call the [MAX6954][1] from now
on. This chip allows me to drive up to 8 16-segment LEDs using one chip and a
minimum of  discrete parts.

The only issue I had with it was that it used a [common cathode][2] multisegment LED
and I was using a [common anode][2] part. I quickly ordered 10 Kingbright 16 segment
single digit common cathode displays (PSC08-11SRWA) and two MAX6954 chips. After
they arrived I connected a single digit display using the sample circuit shown
on [Application Note 3212 Quick-Start: Driving 16-Segment Displays with the
MAX6954][3]. I took a picture after I hooked it up and it looked like this after
I wrote some code using the previous SPI driver code to put the chip into
Display Test mode (0x0701).

![Display Test Mode][4]

Single Digit Demo
=================

The MAX6954 contains a mapping of character codes to LED segments which roughly
follows the ASCII standard. I wanted to write a demo program which would allow
me to manipulate the display without too much trouble. Since I had the SPI code
already written I just need to slap on a user interface and experiment once that
was done. I wired up the hardware and wrote the software and tested the unit.
Things looked good until I got to the letter "B".

![Error on Letter "B"][5]

You can see that one of the legs isn't correct. A quick wiring change later and
everything works according to plan!

What's Next?
============

Now that I've got it working for a single digit I need to prototype the full
eight 16 segment displays.

[1]: http://www.maximintegrated.com/en/products/power/display-power-control/MAX6954.html
[2]: http://www.differencebetween.com/difference-between-common-anode-and-vs-common-cathode/
[3]: http://www.maximintegrated.com/en/app-notes/index.mvp/id/3212
[4]: {{ site.url }}/img/project/pinball/single_multisegment_display_01.jpg
[5]: {{ site.url }}/img/project/pinball/single_multisegment_display_02.jpg
