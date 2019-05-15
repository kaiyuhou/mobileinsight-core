#!/usr/bin/python
import utils_enl as enl

from mobile_insight.monitor import OfflineReplayer

from mobile_insight.analyzer import MsgLogger, LteRrcAnalyzer, WcdmaRrcAnalyzer, LteNasAnalyzer, UmtsNasAnalyzer, LtePhyAnalyzer, LteMacAnalyzer

if __name__ == "__main__":
    src = OfflineReplayer()
    src.set_input_path("../logs/monitor-example.mi2log")

    # input_file = utils.get_log_path() + 'monitor-example.mi2log'
    # print(input_file)
    # # output_file = input_file + ".xml"
    #



    # # #
    lte_nas_analyzer = LteNasAnalyzer()
    lte_nas_analyzer.set_source(src)

    print("Hello World")
    dumper = MsgLogger()
    dumper.set_source(src)
    dumper.set_decoding(MsgLogger.XML)

    # # # # umts_nas_analyzer = UmtsNasAnalyzer()
    # # # # umts_nas_analyzer.set_source(src)
    # # # #
    # # # # lte_phy_analyzer = LtePhyAnalyzer()
    # # # # lte_phy_analyzer.set_source(src)
    # # # #
    # # # # lte_mac_analyzer = LteMacAnalyzer()
    # # # # lte_mac_analyzer.set_source(src)
    # # #
    # # # # Start the monitoring
    src.run()
