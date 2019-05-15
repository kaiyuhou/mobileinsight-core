#!/usr/bin/env bash

sudo modprobe usbserial vendor=0x05c6 product=0x9091

sudo python ~/mi-dev/mobileinsight-core/user/monitor-lte-nas.py /dev/ttyUSB0 9600