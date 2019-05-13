#!/usr/bin/python
# Filename: monitor-example.py
import os
import sys

# Import MobileInsight modules
from mobile_insight.monitor import OnlineMonitor
from mobile_insight.analyzer import MsgLogger

if __name__ == "__main__":
    file_in = "/home/kaiyu/mi-dev/mobileinsight-core/logs/monitor-example.mi2log"
    file_out = file_in + '.xml'

    if len(sys.argv) < 3:
        print "Error: please specify physical port name and baudrate."
        print __file__, "SERIAL_PORT_NAME BAUNRATE"
        sys.exit(1)

    src = OnlineMonitor()
    src.set_serial_port(sys.argv[1])  # the serial port to collect the traces
    src.set_baudrate(int(sys.argv[2]))  # the baudrate of the port

    # Save the monitoring results as an offline log
    src.save_log_as(file_in)

    # Enable 3G/4G messages to be monitored. Here we enable RRC (radio
    src.enable_log("LTE_NAS_EMM_OTA_Incoming_Packet")
    src.enable_log("LTE_NAS_EMM_OTA_Outgoing_Packet")
    src.enable_log("LTE_NAS_EMM_State")
    src.enable_log("LTE_NAS_ESM_OTA_Incoming_Packet")
    src.enable_log("LTE_NAS_ESM_OTA_Incoming_Packet")
    src.enable_log("LTE_NAS_ESM_OTA_Incoming_Packet")
    src.enable_log("LTE_NAS_ESM_OTA_Outgoing_Packet")
    src.enable_log("LTE_NAS_ESM_State")

    # Dump the messages to std I/O. Comment it if it is not needed.
    logger = MsgLogger()

    # logger.set_decode_format(MsgLogger.JSON)
    logger.set_decode_format(MsgLogger.XML)
    logger.set_dump_type(MsgLogger.FILE_ONLY)
    logger.save_decoded_msg_as(file_out)
    logger.set_source(src)

    # Start the monitoring
    src.run()
