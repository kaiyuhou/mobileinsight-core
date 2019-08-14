import time
import platform
import os


class Carrier():
    Verizon = 'Verizon'
    ATT = 'ATT'
    TMobile = 'TMobile'
    Sprint = 'Sprint'
    CM = 'CM'


class Cell_Phone():
    RedMi_Note4X = 'RedMi-Note4X'


def get_log_path():
    if platform.system() == 'Windows':
        return 'D:/workspace/mobileinsight-core/logs/'

    return "/home/kaiyu/mi-dev/mobileinsight-core/logs/"


def time_to_str(t):
    if t < 10:
        return '0' + str(t)
    else:
        return str(t)


def file_name_mi2(carrier, phone, case=''):
    local_time = time.localtime()
    file_name = ['mi2']

    file_name.append(time_to_str(local_time.tm_mon) + time_to_str(local_time.tm_mday))
    file_name.append(time_to_str(local_time.tm_hour) + time_to_str(local_time.tm_min) + time_to_str(local_time.tm_sec))
    file_name.append(carrier)
    file_name.append(phone)

    if case:
        file_name.append(case)

    filename = get_log_path() + '_'.join(file_name) + '.mi2log'

    with open(get_log_path() + 'record.csv', 'a') as f:
        record = []
        record.append(filename.split('/')[-1])
        record.append(carrier)
        record.append(phone)
        record.append(case)
        f.write(','.join(record))
        f.write('\n')

    return filename


def enable_nas_log(src):
    src.enable_log("LTE_NAS_EMM_OTA_Incoming_Packet")
    src.enable_log("LTE_NAS_EMM_OTA_Outgoing_Packet")
    src.enable_log("LTE_NAS_EMM_State")
    src.enable_log("LTE_NAS_ESM_OTA_Incoming_Packet")
    src.enable_log("LTE_NAS_ESM_OTA_Outgoing_Packet")
    src.enable_log("LTE_NAS_ESM_State")


def file_name_xml(name):
    return get_log_path() + 'xml' + name[len(get_log_path()) + 3:-6] + 'xml'


if __name__ == '__main__':
    # print(file_name_mi2(Carrier.Verizon, Cell_Phone.RedMi_Note4X))
    print(file_name_xml(file_name_mi2(Carrier.Verizon, Cell_Phone.RedMi_Note4X)))
    # print(get_log_path())
