---
layout: post
title:  "Investigating the SPI driver"
---

We [left off][1] with the hardware being hooked up but no software to run our
project. I wanted to test the SPI hardware and the best way to do so is with a
[loopback][2] test. After using my favorite search engine I found a post called
[SPI-Python: Hardware SPI for RasPi from Python][3] by Louis Thiery. He had an
interesting article on how to interface an Arduino with a RasPi. I wasn't
interested in that (right now) but I was curious about the spidev_test program
that he used to verify his setup. However, the instructions didn't work for me
due URLs I couldn't get to and a test program that wouldn't compile because of
differences in the header files.

Modifying the Code
==================

On my Raspberry Pi I created a directory in which to load the source file and
then I got the original source from the Linux source tree.

    mkdir spidev_test
    wget https://raw.githubusercontent.com/torvalds/linux/master/Documentation/spi/spidev_test.c

I now had the tester source file in my directory. It's a simple matter to
compile it.

    gcc spidev_test.c -o spidev_test

Uh oh, I get a few error messages:

    spidev_test.c: In function ‘transfer’:
    spidev_test.c:60:13: error: ‘SPI_TX_QUAD’ undeclared (first use in this function)
    spidev_test.c:60:13: note: each undeclared identifier is reported only once for each function it appears in
    spidev_test.c:61:5: error: ‘struct spi_ioc_transfer’ has no member named ‘tx_nbits’
    spidev_test.c:62:18: error: ‘SPI_TX_DUAL’ undeclared (first use in this function)
    spidev_test.c:63:5: error: ‘struct spi_ioc_transfer’ has no member named ‘tx_nbits’
    spidev_test.c:64:13: error: ‘SPI_RX_QUAD’ undeclared (first use in this function)
    spidev_test.c:65:5: error: ‘struct spi_ioc_transfer’ has no member named ‘rx_nbits’
    spidev_test.c:66:18: error: ‘SPI_RX_DUAL’ undeclared (first use in this function)
    spidev_test.c:67:5: error: ‘struct spi_ioc_transfer’ has no member named ‘rx_nbits’
    spidev_test.c: In function ‘parse_opts’:
    spidev_test.c:172:12: error: ‘SPI_TX_DUAL’ undeclared (first use in this function)
    spidev_test.c:175:12: error: ‘SPI_TX_QUAD’ undeclared (first use in this function)
    spidev_test.c:184:12: error: ‘SPI_RX_DUAL’ undeclared (first use in this function)
    spidev_test.c:186:12: error: ‘SPI_RX_QUAD’ undeclared (first use in this function)
    spidev_test.c: In function ‘main’:
    spidev_test.c:204:18: error: ‘SPI_IOC_WR_MODE32’ undeclared (first use in this function)
    spidev_test.c:208:18: error: ‘SPI_IOC_RD_MODE32’ undeclared (first use in this function)

After some investigation the culprit turns out to be my spidev.h header file.
The constants mentioned above don't exist in that file. I am using **Linux
raspberrypi 3.18.7+** and as of that distribution those constants are not there.
When I check the file on github the commit log says that the new revision
implements a couple of new modes for [DMA][4] controlled SPI. Ah, well I don't
care about that so I'll just comment out references to those constants.

As an aside, unless you are doing **a lot** of SPI reads (or writes) you
probably don't need a DMA interface.

The last thing is the change the name of the device file from /dev/spidev1.1 to
/dev/spidev0.0

Once the references were commented out and the device file updaed it compiled
fine. Now, on to the test.

Testing the Loopback
====================

The first thing I need to do is to connect the loopback. This is very simple
since I'm using a breadboard and the [Adafruit T-Cobbler Plus][5]. I just put a
jumper from the MOSI (Master Out Slave In) to MISO (Master In Slave Out). Now
we're ready to run the code!

To run the code I used the sudo utility since accessing hardware directly is not
normally allowed in Linux. I ran the code and observed the output.

    pi@raspberrypi:~/spidev_test$ sudo ./spidev_test

This is what I saw. It works!

    spi mode: 0x0
    bits per word: 8
    max speed: 500000 Hz (500 KHz)

    FF FF FF FF FF FF
    40 00 00 00 00 95
    FF FF FF FF FF FF
    FF FF FF FF FF FF
    FF FF FF FF FF FF
    DE AD BE EF BA AD
    F0 0D

A Complication
==============

When I was working with the SPI interface I was pushing on it really hard and
after awhile it didn't show up when I rebooted. I first noticed this after I had
done an update to my system using the apt-get two-step.

    sudo apt-get update
    sudo apt-get upgrade

The best way to fix it is to use raspi-config to always enable the SPI
interface. I'm going to be a heavy user of SPI so I don't see why I wouldn't
want to do this. The SPI interface controls are located under the "8 Advanced
Options" entry. Once chosen select "A6 SPI". It will then ask you if you want to
enable the SPI interface and if you want to load the kernel module. Yes to both
questions. Save it and after a reboot you should see the driver when you issue
an **lsmod**

    pi@raspberrypi:~$ lsmod
    Module                  Size  Used by
    snd_bcm2835            21342  0
    snd_pcm                93100  1 snd_bcm2835
    snd_seq                61097  0
    snd_seq_device          7209  1 snd_seq
    snd_timer              23007  2 snd_pcm,snd_seq
    snd                    67211  5 snd_bcm2835,snd_timer,snd_pcm,snd_seq,snd_seq_device
    spi_bcm2708             6018  0
    uio_pdrv_genirq         3666  0
    uio                     9897  1 uio_pdrv_genirq

Now I have the SPI available whenever I start up my Pi.

What's Next
===========

Now that I've got the software test working I want to write some code to send
information to my [4-Wire-Intefaced 20-Port LED Display Driver and I/O Expander
(MAX6957)][6] and light an LED.

[1]: {{ site.url }}/project/pinball/lighting-an-led/
[2]: https://en.wikipedia.org/wiki/Loopback
[3]: http://louisthiery.com/?p=248&preview=true
[4]: https://en.wikipedia.org/wiki/Direct_memory_access
[5]: http://www.adafruit.com/products/2028
[6]: http://datasheets.maximintegrated.com/en/ds/MAX6957.pdf
