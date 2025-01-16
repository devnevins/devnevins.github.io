---
layout: post
title:  "Lighting an LED"
---
If you look at my [first light][1] post there is a glorious picture of a blank breadboard hooked up
to a Raspberry Pi. I got it to flip a bit on the GPIO (#21) but I really wanted to see something.
I'd like to do that classic project, lighting an LED, but with a more useful twist. Rather than
hooking the LED up directly I want to use a
[4-Wire-Intefaced 20-Port LED Display Driver and I/O Expander (MAX6957)][2]
to light my LED. By doing this I would learn how to control the SPI interface
and I should be able to expand my drivers to accommodate my eventual pinball display.

Setting up the hardware
=======================

I needed to connect my MAX6957 to my Raspberry Pi thorugh the SPI interface. The
[Adafruit T-Cobbler Plus][3]
made doing that a dream once I figured out that MOSI meant Master Out Slave In which corresponded to
the MAX6957's DIN port. After that the rest was easy. My schematic looks like this:

![LED lighting setup schematic][4]

I used a 150 Ohm resistor to current limit the LED to about 17mA. The MAX6957 also controls the
current limit but I wanted some hardware reassurance. I might remove it later. We'll see. I quickly
hooked it up; it's a thing of beauty!

![LED lighting breadboard][5]

Next, on to the software.

Setting up the software
=======================

I took a look at the excellent blog post on [100 Random Tasks][6] called
[Simple SPI on Raspberry Pi][7]. This pointed me in the right direction of how to enable the Linux
Kernel module by removing it from the blacklist. The blacklist is used to disable certain kernel
modules and becuase Debian has SPI turned off by default you need to enable it. You can enable it
 by editing **/etc/modprobe.d/raspi-blacklsit.conf**

    sudo vi /etc/modprobe.d/raspi-blacklsit.conf

Once in the file I commented out the blacklist command for the SPI driver. It now looks like this:

    # blacklist spi and i2c by default (many users don't need them)

    # I want to use the SPI interface so I need to turn it on.
    #blacklist spi-bcm2708
    blacklist i2c-bcm2708

After a quick reboot I could see that the module was present by doing an **lsmod**

    pi@raspberrypi:~$ lsmod
    Module                  Size  Used by
    snd_bcm2835            18169  0
    snd_soc_bcm2708_i2s     5486  0
    regmap_mmio             2818  1 snd_soc_bcm2708_i2s
    snd_soc_core          128166  1 snd_soc_bcm2708_i2s
    regmap_spi              1913  1 snd_soc_core
    snd_pcm_dmaengine       5481  1 snd_soc_core
    snd_pcm                81518  3 snd_bcm2835,snd_soc_core,snd_pcm_dmaengine
    snd_page_alloc          5168  1 snd_pcm
    regmap_i2c              1657  1 snd_soc_core
    snd_compress            8136  1 snd_soc_core
    snd_seq                54581  0
    snd_timer              20353  2 snd_pcm,snd_seq
    snd_seq_device          6485  1 snd_seq
    leds_gpio               2055  0
    led_class               4119  1 leds_gpio
    snd                    61518  7 snd_bcm2835,snd_soc_core,snd_timer,snd_pcm,snd_seq,snd_seq_device,snd_compress
    spi_bcm2708             4808  0

It's down there on the bottom and listed as **spi_bcm2708**. But how to use it?!?!?!

[1]: {{ site.url }}/project/pinball/first-light/
[2]: http://datasheets.maximintegrated.com/en/ds/MAX6957.pdf
[3]: http://www.adafruit.com/products/2028
[4]: {{ site.url }}/img/project/pinball/bare_pi.jpg (not correct)
[5]: {{ site.url }}/img/project/pinball/bare_pi.jpg (not correct)
[6]: http://www.100randomtasks.com/
[7]: http://www.100randomtasks.com/simple-spi-on-raspberry-pi
