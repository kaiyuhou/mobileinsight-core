#!/usr/bin/env bash

#/etc/profile
#/etc/environment

export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH=${PATH}:${JAVA_HOME}/bin


sudo modprobe usbserial vendor=0x05c6 product=0x9091

sudo python ~/mi-dev/mobileinsight-core/enl/monitor-lte-nas.py /dev/ttyUSB0 9600

sudo python ~/mi-dev/mobileinsight-core/enl/offline-analysis-lte-nas.py