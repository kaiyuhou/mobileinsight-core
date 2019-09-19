from mobile_insight.monitor import OfflineReplayer
from mobile_insight.analyzer import MsgLogger
from utils_enl import *


def run(path, file):

    src = OfflineReplayer()
    src.set_input_path(path + file)
    enable_nas_log(src)

    logger = MsgLogger()
    logger.set_decode_format(MsgLogger.XML)
    logger.set_dump_type(MsgLogger.FILE_ONLY)
    logger.save_decoded_msg_as(path + file + '.xml')
    logger.set_source(src)
    src.run()

if __name__ == "__main__":
    path = '/home/kaiyu/Desktop/log0/'
    import os
    for f in os.listdir(path):
        if f.endswith('.mi2log'):
            run(path, f)
