import time


class Carrier():
    Verizon = 'Verizon'
    ATT = 'ATT'
    TMobile = 'TMobile'
    Sprint = 'Sprint'


class Cell_Phone():
    RedMi_Note4X = 'RedMi-Note4X'


def get_log_path():
    return "/home/kaiyu/mi-dev/mobileinsight-core/logs/"


def get_file_name(carrier, phone, case=''):
    local_time = time.localtime()
    file_name = []

    if local_time.tm_mon < 10:
        file_name.append('0' + str(local_time.tm_mon) + str(local_time.tm_mday))
    else:
        file_name.append(str(local_time.tm_mon) + str(local_time.tm_mday))

    file_name.append(str(local_time.tm_hour) + str(local_time.tm_min) + str(local_time.tm_sec))
    file_name.append(carrier)
    file_name.append(phone)

    if case:
        file_name.append(case)

    return get_log_path() + '_'.join(file_name) + '.mi2log'


if __name__ == '__main__':
    print(get_file_name(Carrier.Verizon, Cell_Phone.RedMi_Note4X))

