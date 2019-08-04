
import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.1.1','gaurav','VIRL')
iosvl2.open()

# get_mac_address_table() is one of the methods to retrieve mac address table information using napalm class
ios_output = iosvl2.get_mac_address_table()
print(json.dumps(ios_output, indent = 4, sort_keys= True))

with open('mac_address_table_s1.txt', 'w') as mac_sw1:
    mac_sw1.write('\"writing mac address table of sw1\"')
    mac_sw1.write(json.dumps(ios_output, indent = 4, sort_keys = True))

iosvl2.close()
