from mobile_insight.monitor import OfflineReplayer
from mobile_insight.analyzer import MsgLogger
from utils_enl import *


def run(file):

    src = OfflineReplayer()
    src.set_input_path(file)
    enable_nas_log(src)

    logger = MsgLogger()
    logger.set_decode_format(MsgLogger.XML)
    logger.set_dump_type(MsgLogger.STDIO_ONLY)
    # logger.save_decoded_msg_as(file_out)
    logger.set_source(src)
    src.run()

if __name__ == "__main__":
    path = '/home/kaiyu/Desktop/log0/'
    import os
    for f in os.listdir(path):
        run(path + f)
