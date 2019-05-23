import xml.etree.ElementTree as ET
import utils_enl

file_name = utils_enl.get_log_path() + 'xml_0521_192011_Verizon_RedMi-Note4X.xml'

log_pair_key = ['log_msg_len', 'type_id', 'timestamp']

message_type_id =['LTE_NAS_EMM_State',
                  'LTE_NAS_EMM_OTA_Incoming_Packet',
                  'LTE_NAS_EMM_OTA_Outgoing_Packet',
                  'LTE_NAS_ESM_State',
                  'LTE_NAS_ESM_OTA_Incoming_Packet',
                  'LTE_NAS_ESM_OTA_Outgoing_Packet']

LTE_NAS_EMM_State_keywords = ['PLMN', 'GUTI PLMN', 'EMM State']
LTE_NAS_ESM_State_keywords = ['EPS bearer state']
LTE_NAS_Packet_keywords = ['nas_eps.nas_msg_emm_type',
                           'nas_eps.emm.eps_att_type',
                           'nas_eps.emm.type_of_id',
                           'e212.mcc',
                           'e212.mnc']

message_keywords = {
            'LTE_NAS_EMM_State': LTE_NAS_EMM_State_keywords,
            'LTE_NAS_ESM_State': LTE_NAS_ESM_State_keywords,
            }

def _parse_LTE_NAS_state(pairs):
    msg_type = pairs[1].text
    rnt_msg = [msg_type]
    for i, pair in enumerate(pairs):
        assert pair.tag == 'pair', "pair.tag == 'pair'"
        assert 'key' in pair.attrib.keys()

        key = pair.attrib['key']
        if key in message_keywords[msg_type]:
            rnt_msg.append(key + ": " + pair.text)
    return rnt_msg

def _parse_LTE_NAS_Packet(packet):
    rnt_msg = []
    for proto in packet.getchildren():
        assert proto.tag == 'proto'
        assert 'name' in proto.attrib.keys()

        if 'nas' not in proto.attrib['name']:
            continue

        def _dfs_field(field):
            assert 'name' in field.attrib.keys()
            if field.attrib['name'] in LTE_NAS_Packet_keywords:
                msg = '\n\t' + field.attrib['name'] + ': ' + field.attrib['showname']


                if 'value' in field.attrib.keys():
                    msg += ': ' + field.attrib['value']
                rnt_msg.append(msg)
            for c_field in field.getchildren():
                _dfs_field(c_field)

        for field in proto.getchildren():
            _dfs_field(field)


    return rnt_msg



def parse_LTE_NAS_EMM_State(pairs):
    return _parse_LTE_NAS_state(pairs)

def parse_LTE_NAS_ESM_State(pairs):
    return _parse_LTE_NAS_state(pairs)

def parse_LTE_NAS_EMM_OTA_Incoming_Packet(pairs):
    pass

def parse_LTE_NAS_EMM_OTA_Outgoing_Packet(pairs):
    msg_type = pairs[1].text
    rnt_msg = [msg_type]
    for i, pair in enumerate(pairs):
        assert pair.tag == 'pair', "pair.tag == 'pair'"
        assert 'key' in pair.attrib.keys()

        key = pair.attrib['key']
        if key != 'Msg':
            continue

        for msg in pair.getchildren():
            assert msg.tag == 'msg'
            for packet in msg.getchildren():
                assert packet.tag == 'packet'
                rnt_msg += _parse_LTE_NAS_Packet(packet)





    return rnt_msg

def parse_LTE_NAS_ESM_OTA_Incoming_Packet(pairs):
    pass

def parse_LTE_NAS_ESM_OTA_Outgoing_Packet(pairs):
    pass

def parse_dm_packet(pairs):
    type_parse = {
        'LTE_NAS_EMM_State': parse_LTE_NAS_EMM_State,
        'LTE_NAS_EMM_OTA_Incoming_Packet': parse_LTE_NAS_EMM_OTA_Incoming_Packet,
        'LTE_NAS_EMM_OTA_Outgoing_Packet': parse_LTE_NAS_EMM_OTA_Outgoing_Packet,
        'LTE_NAS_ESM_State': parse_LTE_NAS_ESM_State,
        'LTE_NAS_ESM_OTA_Incoming_Packet': parse_LTE_NAS_ESM_OTA_Incoming_Packet,
        'LTE_NAS_ESM_OTA_Outgoing_Packet': parse_LTE_NAS_ESM_OTA_Outgoing_Packet,
    }

    return type_parse[pairs[1].text](pairs)


if __name__ == '__main__':
    et = ET.fromstring('<mi2>' + '</mi2>')
    ans = []
    with open(file_name) as f:
        et = ET.fromstring('<mi2>' + f.read() + '</mi2>')
    for dm_packet in et.getchildren():
        pairs = dm_packet.getchildren()
        assert pairs[1].text in message_type_id

        msg = parse_dm_packet(pairs)
        if msg:
            ans.append(', '.join(msg))

    print('\n'.join(ans))








            # assert
    # assert True == False, 'Finish'


        # for pair in child.getchildren():
            # print(pair.tag)
            # assert pairs[]

            # print('%s : %s' % (pair.attrib['key'], pair.text))
            # print(pair.text)
            # for ele in pair.getchildren():
            #     print('has ele')

# tree = ET.ElementTree(file=file_name)
