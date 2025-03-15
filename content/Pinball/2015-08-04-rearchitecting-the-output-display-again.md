---
title:  Rearchitecting the output display, again.
date: 2015-08-04
category: Pinball
---

The Problem
===========
I want to create some simple circuit diagrams that look nice and can also be
used to create a circuit board. Most layout programs either cost big bucks or
run on the PC only (and still cost big bucks). I found a tool aimed primarily at
Arduino called [Fritzing][1] but I found that the parts catalog is fairly
minimal (except for [Sparkfun][2] parts) and making new parts for it is quite a
pain. Additionally, Fritzing provides a board layout service but their terms for
shipment to the U.S. are pretty terrible.

I then found a package called [EAGLE][3] which seemed like a very capable
package but unfortunately for me I could either use the hobbyist version which
produced tiny boards or I could use the professional version which produced huge
boards but cost over $1,000. I can see paying for a tool like this if I spent
most of my time (or even alot) making boards but I don't so that seemed a bit
steep.

I found a really nice tool (so far) called [pcbweb][4]. It is tied into the
Digi-Key catalog which I personally find to be an advantage. Since I'm doing
breadboarding they don't have a lot of parts built into the library using the
through-hole form package. This however is mitigated quite a bit by the fact
that making new parts is **way** easier than any other tool that I've used.
It's very sensible and doesn't require you to use a bunch of external programs.

Yet Another Pivot
=================
I've been looking at my current circuit for driving the display and it seems to
me to be not really that great. It's expensive with the drivers alone costing
$27 a piece and each will require an SPI connection or a bus mechanic which I'm
not fond of. I would like to keep an intelligent interface, preferably
[RS-485][5] based and put a lot of intelligence into the board itself.
Therefore, I've decided to do a different design using a [PIC16F684][6] chip and
some discrete drivers.

An initial challenge is going to be using the PIC chip since it only has about
12 I/O lines to play with. I'm going to take a bussed approach where I use the
*relatively* high current drive capacity of the 16F684 to put a lot of chips on
a bus and do some clever things with clocking.

Next Steps
==========
I need to create a circuit for one LED to prove the concept. I'll also be
writing some PIC16F684 code. I haven't decided if I'm going to do it in assembly
or C. C would be easier but assembly might be more interesting.

[1]: http://fritzing.org/home/
[2]: https://www.sparkfun.com
[3]: http://www.cadsoftusa.com
[4]: http://www.pcbweb.com
[5]: https://en.wikipedia.org/wiki/RS-485
[6]: http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010214
