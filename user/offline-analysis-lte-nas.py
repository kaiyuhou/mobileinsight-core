#!/usr/bin/python
import os
import sys
import utils

"""
Offline analysis by replaying logs
"""

# Import MobileInsight modules
from mobile_insight.monitor import OfflineReplayer
# from mobile_insight.analyzer import MsgLogger, LteRrcAnalyzer, WcdmaRrcAnalyzer, LteNasAnalyzer, UmtsNasAnalyzer, LtePhyAnalyzer, LteMacAnalyzer

if __name__ == "__main__":

    input_file = utils.get_log_path() + 'monitor-example.mi2log'
    print(input_file)
    # output_file = input_file + ".xml"

    # # Initialize a 3G/4G monitor
    # src = OfflineReplayer()
    # src.set_input_path(input_file)
    # #
    # # src.enable_log("LTE_NAS_EMM_OTA_Incoming_Packet")
    # # src.enable_log("LTE_NAS_EMM_OTA_Outgoing_Packet")
    # #
    # # # lte_nas_analyzer = LteNasAnalyzer()
    # # # lte_nas_analyzer.set_source(src)
    # #
    # # # umts_nas_analyzer = UmtsNasAnalyzer()
    # # # umts_nas_analyzer.set_source(src)
    # # #
    # # # lte_phy_analyzer = LtePhyAnalyzer()
    # # # lte_phy_analyzer.set_source(src)
    # # #
    # # # lte_mac_analyzer = LteMacAnalyzer()
    # # # lte_mac_analyzer.set_source(src)
    # #
    # # # Start the monitoring
    # src.run()
