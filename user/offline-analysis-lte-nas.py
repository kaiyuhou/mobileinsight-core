#!/usr/bin/python
# Filename: offline-analysis-example.py
import os
import sys

"""
Offline analysis by replaying logs
"""

# Import MobileInsight modules
from mobile_insight.monitor import OfflineReplayer
from mobile_insight.analyzer import MsgLogger, LteRrcAnalyzer, WcdmaRrcAnalyzer, LteNasAnalyzer, UmtsNasAnalyzer, LtePhyAnalyzer, LteMacAnalyzer

if __name__ == "__main__":



    input_file = "../logs/0512_185900_Verizon_RedmiNote4X.mi2log"
    output_file = input_file + ".xml"

    # Initialize a 3G/4G monitor
    src = OfflineReplayer()
    src.set_input_path(input_file)

    src.enable_log("LTE_RRC_OTA_Packet")
    # src.enable_log("WCDMA_RRC_OTA_Packet")
    # src.enable_log("WCDMA_RRC_Serv_Cell_Info")

    logger = MsgLogger()

    # logger.set_decode_format(MsgLogger.JSON)
    logger.set_decode_format(MsgLogger.XML)
    logger.set_dump_type(MsgLogger.FILE_ONLY)
    logger.save_decoded_msg_as(output_file)
    logger.set_source(src)

    # # Analyzers
    lte_rrc_analyzer = LteRrcAnalyzer()
    lte_rrc_analyzer.set_source(src)  # bind with the monitor

    # wcdma_rrc_analyzer = WcdmaRrcAnalyzer()
    # wcdma_rrc_analyzer.set_source(src)  # bind with the monitor
    #
    # lte_nas_analyzer = LteNasAnalyzer()
    # lte_nas_analyzer.set_source(src)
    #
    # umts_nas_analyzer = UmtsNasAnalyzer()
    # umts_nas_analyzer.set_source(src)
    #
    # lte_phy_analyzer = LtePhyAnalyzer()
    # lte_phy_analyzer.set_source(src)
    #
    # lte_mac_analyzer = LteMacAnalyzer()
    # lte_mac_analyzer.set_source(src)

    # Start the monitoring
    src.run()
