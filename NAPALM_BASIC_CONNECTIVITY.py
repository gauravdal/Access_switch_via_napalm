import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.1.1','gaurav','VIRL')
iosvl2.open()

# get_facts() is one of the methods to retrieve information using napalm class
ios_output = iosvl2.get_facts()
print(json.dumps(ios_output, indent = '4', sort_keys= True))




#get_interfaces is one of the methods to retreive interfaces information
ios_output = iosvl2.get_interfaces
print(json.dumps(ios_output, indent = '4', sort_keys= True))

# get_interfaces_counters is a method to retreive number of interfaces
ios_output = iosvl2.get_interfaces_counters()
print(json.dumps(ios_output, indent = '4', sort_keys= True))

iosvl2.close()