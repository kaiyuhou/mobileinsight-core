from mobile_insight.monitor import OfflineReplayer
from mobile_insight.analyzer import MsgLogger
from utils_enl import *


def run(file):
    path = '/home/kaiyu/Desktop/log0/'

    # Initialize a 3G/4G monitor
    src = OfflineReplayer()

    # src.set_input_path(get_log_path() + "mi2_0521_192011_Verizon_RedMi-Note4X.mi2log")
    src.set_input_path(path + "diag_log_20190917_134318_8555e5d060cb619dd377f7db1f7e64ce_Letv-X800_.mi2log")

    # src.save_log_as(get_log_path() + "filtered_log.mi2log")

    print(get_log_path())

    enable_nas_log(src)

    logger = MsgLogger()
    logger.set_decode_format(MsgLogger.XML)
    logger.set_dump_type(MsgLogger.STDIO_ONLY)
    # logger.save_decoded_msg_as(file_out)
    logger.set_source(src)

    # Start the monitoring
    src.run()

if __name__ == "__main__":
    # file_in = file_name_mi2(Carrier.Verizon, Cell_Phone.RedMi_Note4X)
    # file_out = file_name_xml(file_in)
    path = '/home/kaiyu/Desktop/log0/'


    # Initialize a 3G/4G monitor
    src = OfflineReplayer()

    # src.set_input_path(get_log_path() + "mi2_0521_192011_Verizon_RedMi-Note4X.mi2log")
    src.set_input_path(path + "diag_log_20190917_134318_8555e5d060cb619dd377f7db1f7e64ce_Letv-X800_.mi2log")

    # src.save_log_as(get_log_path() + "filtered_log.mi2log")

    print(get_log_path())

    enable_nas_log(src)

    logger = MsgLogger()
    logger.set_decode_format(MsgLogger.XML)
    logger.set_dump_type(MsgLogger.STDIO_ONLY)
    # logger.save_decoded_msg_as(file_out)
    logger.set_source(src)

    # Start the monitoring
    src.run()
