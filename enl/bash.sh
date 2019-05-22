#!/usr/bin/env bash

sudo modprobe usbserial vendor=0x05c6 product=0x9091

sudo python ~/mi-dev/mobileinsight-core/enl/monitor-lte-nas.py /dev/ttyUSB0 9600

sudo python ~/mi-dev/mobileinsight-core/enl/offline-analysis-lte-nas.py