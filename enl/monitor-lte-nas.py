import sys
import utils_enl

# Import MobileInsight modules
from mobile_insight.monitor import OnlineMonitor
from mobile_insight.analyzer import MsgLogger

if __name__ == "__main__":
    file_in = utils_enl.file_name_mi2(utils_enl.Carrier.TMobile, utils_enl.Cell_Phone.RedMi_Note4X)
    file_out = utils_enl.file_name_xml(file_in)



    if len(sys.argv) < 3:
        print "Error: please specify physical port name and baudrate."
        print __file__, "SERIAL_PORT_NAME BAUNRATE"
        sys.exit(1)

    src = OnlineMonitor()
    src.set_serial_port(sys.argv[1])  # the serial port to collect the traces
    src.set_baudrate(int(sys.argv[2]))  # the baudrate of the port

    # Save the monitoring results as an offline log
    src.save_log_as(file_in)

    utils_enl.enable_nas_log(src)

    logger = MsgLogger()
    logger.set_decode_format(MsgLogger.XML)
    logger.set_dump_type(MsgLogger.ALL)
    logger.save_decoded_msg_as(file_out)
    logger.set_source(src)

    # Start the monitoring
    src.run()
