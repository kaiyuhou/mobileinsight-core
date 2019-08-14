import xml.etree.ElementTree as ET
import utils_enl

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
                           'nas_eps.nas_msg_esm_type',
                           'nas_eps.emm.eps_att_type',
                           'nas_eps.emm.type_of_id',
                           'e212.mcc',
                           'e212.mnc',
                           'nas_eps.emm.mme_grp_id',
                           'nas_eps.emm.mme_code',
                           'nas_eps.nas_msg_esm_type',
                           'nas_eps.esm_request_type',
                           'ipcp.opt.pri_dns_address',
                           'ipcp.opt.sec_dns_address',
                           'nas_eps.emm.EPS_attach_result',
                           'gsm_a.gm.sm.apn',
                           'nas_eps.emm.cause',
                           'gsm_a.dtap.text_string',
                           'gsm_a.dtap.time_zone_time',
                           'gsm_a.dtap.dst_adjustment',
                           'gsm_a.dtap.emergency_number_information',
                           'gsm_a.dtap.emerg_num_info_length',
                           'gsm_a.dtap.serv_cat_b5',
                           'gsm_a.dtap.serv_cat_b4',
                           'gsm_a.dtap.serv_cat_b3',
                           'gsm_a.dtap.serv_cat_b2',
                           'gsm_a.dtap.serv_cat_b1',
                           'gsm_a.dtap.emergency_bcd_num',
                           'nas_eps.security_header_type',
                           'gsm_a.ie.mobileid.type',
                           'gsm_a.imeisv',
                           'gsm_a.tmsi',]

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
            rnt_msg.append((key, pair.text))
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
                if 'value' in field.attrib.keys():
                    msg = (field.attrib['name'], field.attrib['showname'], field.attrib['value'])
                else:
                    msg = (field.attrib['name'], field.attrib['showname'])
                rnt_msg.append(msg)

            for c_field in field.getchildren():
                _dfs_field(c_field)

        for field in proto.getchildren():
            _dfs_field(field)

    return rnt_msg

def _parse_LTE_NAS_Packet_Pair(pairs):
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

def parse_LTE_NAS_EMM_OTA_Incoming_Packet(pairs):
    return _parse_LTE_NAS_Packet_Pair(pairs)

def parse_LTE_NAS_EMM_OTA_Outgoing_Packet(pairs):
    return _parse_LTE_NAS_Packet_Pair(pairs)

def parse_LTE_NAS_ESM_OTA_Incoming_Packet(pairs):
    return _parse_LTE_NAS_Packet_Pair(pairs)

def parse_LTE_NAS_ESM_OTA_Outgoing_Packet(pairs):
    return _parse_LTE_NAS_Packet_Pair(pairs)

def parse_dm_packet(pairs):
    type_parse = {
        'LTE_NAS_EMM_State': _parse_LTE_NAS_state,
        'LTE_NAS_EMM_OTA_Incoming_Packet': parse_LTE_NAS_EMM_OTA_Incoming_Packet,
        'LTE_NAS_EMM_OTA_Outgoing_Packet': parse_LTE_NAS_EMM_OTA_Outgoing_Packet,
        'LTE_NAS_ESM_State': _parse_LTE_NAS_state,
        'LTE_NAS_ESM_OTA_Incoming_Packet': parse_LTE_NAS_ESM_OTA_Incoming_Packet,
        'LTE_NAS_ESM_OTA_Outgoing_Packet': parse_LTE_NAS_ESM_OTA_Outgoing_Packet,
    }

    assert pairs[1].text in message_type_id
    return type_parse[pairs[1].text](pairs)


def packet_to_string(packet):
    msg = ''
    if packet[0] in ['LTE_NAS_EMM_State', 'LTE_NAS_ESM_State']:
        msg = ', '.join([str(item) for item in packet])
    else:
        msg = '\n\t'.join([str(item) for item in packet])
    return msg


def ans_to_string(ans):
    msg = ''
    for packet in ans:
        if not packet:
            continue
        msg += packet_to_string(packet) + '\n'
    return msg


def strip_punctuation(S):
    S = S.replace('(', '')
    S = S.replace(')', '')
    S = S.replace('\'', '')
    return S


def remove_redundant_packet(packets):
    ans = []
    for p in packets:
        if p not in ans:
            ans.append(p)
    return ans

def simple_message(S):
    simple = {
        'EMM State, ': '',
        'nas_eps.security_header_type, 0000 .... = Security header type: ': 'Security Type: ',
        'nas_eps.nas_msg_emm_type, NAS EPS Mobility Management Message Type: ': 'Message Type: ',
        'nas_eps.emm.eps_att_type, .... .010 = EPS attach type: ': 'EPS attach type: ',
        'nas_eps.emm.type_of_id, .... .110 = Type of identity: ': 'Type of identity: ',
        'e212.mcc, Mobile Country Code ': '',
        '\n\te212.mnc, Mobile Network Code ': '\t',
        'nas_eps.emm.mme_grp_id, ': '',
        '\n\tnas_eps.emm.mme_code, ': '\t',
        'ipcp.opt.pri_dns_address, ': '',
        '\n\tipcp.opt.sec_dns_address, ': '\t',
        'DNS Address': 'DNS',
        'nas_eps.nas_msg_esm_type, NAS EPS session management messages: ': '',
        'gsm_a.dtap.emergency_bcd_num, ': '** ',
        'gsm_a.dtap.emergency_number_information, ': '** ',
        'gsm_a.dtap.serv_cat_b5, ...1 .... = ': '** ',
        'gsm_a.dtap.serv_cat_b4, .... 1... = ': '** ',
        'gsm_a.dtap.serv_cat_b3, .... .1.. = ': '** ',
        'gsm_a.dtap.serv_cat_b2, .... ..1. = ': '** ',
        'gsm_a.dtap.serv_cat_b1, .... ...1 = ': '** ',
        'gsm_a.dtap.emerg_num_info_length, ': '** ',

    }

    for k,v in simple.items():
        S = S.replace(k, v)
    return S


def remove_ans_value(ans):
    for p in ans:
        for i in range(len(p)):
            if len(p[i]) == 3:
                p[i] = p[i][:-1]
    return ans

def xml_analysis_pipeline(file_in):
    et = ET.fromstring('<mi2>' + '</mi2>')
    ans = []
    with open(file_in) as f:
        et = ET.fromstring('<mi2>' + f.read() + '</mi2>')
    for dm_packet in et.getchildren():
        pairs = dm_packet.getchildren()
        ans.append(parse_dm_packet(pairs))

    ans = remove_redundant_packet(ans)
    ans = remove_ans_value(ans)

    ans_string = ans_to_string(ans)
    ans_string = strip_punctuation(ans_string)
    ans_string = simple_message(ans_string)

    return ans_string

if __name__ == '__main__':
    # file_name = utils_enl.get_log_path() + 'xml_0521_20532_Verizon_RedMi-Note4X.xml'
    # file_name = utils_enl.get_log_path() + 'xml_0521_192011_Verizon_RedMi-Note4X.xml'
    #file_name = utils_enl.get_log_path() + 'xml_0521_193046_Verizon_RedMi-Note4X.xml'
    file_name = utils_enl.get_log_path() + 'xml_0602_234331_CM_RedMi-Note4X.xml'
    print(xml_analysis_pipeline(file_name))






