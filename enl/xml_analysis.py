import xml.etree.ElementTree as ET

file_name = '/home/kaiyu/mi-dev/mobileinsight-core/logs/xml_0521_20532_Verizon_RedMi-Note4X.xml'


if __name__ == '__main__':
    et = ET.fromstring('<mi2>' + '</mi2>')
    with open(file_name) as f:
        et = ET.fromstring('<mi2>' + f.read() + '</mi2>')
    for child in et.getchildren()[0:1]:
        for pair in child.getchildren():
            print(pair.tag)
            print('%s : %s' % (pair.attrib['key'], pair.text))
            # print(pair.text)
            for ele in pair.getchildren():
                print('has ele')

# tree = ET.ElementTree(file=file_name)
