import xml.etree.ElementTree as ET
import utils_enl

file_name = utils_enl.get_log_path() + 'xml_0521_20532_Verizon_RedMi-Note4X.xml'

log_pair_key = ['log_msg_len', 'type_id', 'timestamp']
message_type_id =['LTE_NAS_EMM_State',
                  'LTE_NAS_EMM_OTA_Incoming_Packet',
                  'LTE_NAS_EMM_OTA_Outgoing_Packet',
                  'LTE_NAS_ESM_State',
                  'LTE_NAS_ESM_OTA_Incoming_Packet',
                  'LTE_NAS_ESM_OTA_Outgoing_Packet']

if __name__ == '__main__':
    et = ET.fromstring('<mi2>' + '</mi2>')
    with open(file_name) as f:
        et = ET.fromstring('<mi2>' + f.read() + '</mi2>')
    for dm_packet in et.getchildren():
        pairs = dm_packet.getchildren()
        for i, key in enumerate(log_pair_key):
            assert pairs[i].tag == 'pair', "pairs[i].tag == 'pair'"
            assert pairs[i].attrib['key'] == key, "pairs[i].attrib['key'] == key"


            # assert
    assert True == False, 'Finish'
    

        # for pair in child.getchildren():
            # print(pair.tag)
            # assert pairs[]

            # print('%s : %s' % (pair.attrib['key'], pair.text))
            # print(pair.text)
            # for ele in pair.getchildren():
            #     print('has ele')

# tree = ET.ElementTree(file=file_name)
