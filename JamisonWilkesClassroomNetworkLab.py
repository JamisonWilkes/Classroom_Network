#classroom 1 --30
#classroom 2-- 30
#classroom 3 - 14
#classroom 4 - 14
#classroom 5 - 14
#lab 1 - 6
#lab 2 - 6

#138.191.0.0/25 Total Addresses 128
# Address Range 138.191.0.0 - 138.191.0.127
# Break this address range up into 4 subnets

import ipaddress
import time

ipInterface = ipaddress.ip_interface('138.191.0.0/25')
ipNetwork = ipInterface.network

classroom = list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff = 2))
#138.191.0.0/27  Address Range 138.191.0.1 - 138.191.0.30
#138.191.0.32/27  Address Range 138.191.0.33 - 138.191.0.62
#192.191.0.64/27  Address Range 138.191.0.65 - 138.191.0.94
#192.191.0.96/27  Address Range 138.191.0.97 - 138.191.0.126

#print(classroom[0])
#print(classroom[1])
#print(classroom[2])
#print(classroom[3])

#print('classrooms with 14 computers')
Classroom3 = (list(ipaddress.ip_network(classroom[2]).subnets()))
Classroom4 = (list(ipaddress.ip_network(classroom[3]).subnets()))

#print(Classroom3[0])
#print(Classroom3[1])
#print(Classroom4[0])
#print(Classroom4[1])

#print('labs')
#print(' ')

lab = (list(ipaddress.ip_network(Classroom3[1]).subnets()))
#print(lab[0])
#print(lab[1])

print('IP addresses and network information for assignment')
print('---------------------------------------------------')
print('Lab 1')
print('------------')
print('Lab1 Network Address: {}'.format((lab[0]).network_address))
print('Lab1 Broadcast Address: {}'.format((lab[0]).broadcast_address))
print('Lab1 # of hosts: {}'.format(len(list((lab[0]).hosts()))))
print('Lab1 valid host range: {0} - {1}'.format((((lab[0]).network_address)+1), (((lab[0]).broadcast_address)-1)))

print(' ')
print('Lab 2')
print('------------')
print('Lab2 Network Address: {}'.format((lab[1]).network_address))
print('Lab2 Broadcast Address: {}'.format((lab[1]).broadcast_address))
print('Lab2 # of hosts: {}'.format(len(list((lab[1]).hosts()))))
print('Lab2 valid host range: {0} - {1}'.format((((lab[1]).network_address)+1), (((lab[1]).broadcast_address)-1)))

print(' ')
print('Classroom 3')
print('------------')
print('Classroom3 Network Address: {}'.format((Classroom3[0]).network_address))
print('Classroom3 Broadcast Address: {}'.format((Classroom3[0]).broadcast_address))
print('Classroom3 # of hosts: {}'.format(len(list((Classroom3[0]).hosts()))))
print('Classroom3 valid host range: {0} - {1}'.format((((Classroom3[0]).network_address)+1), (((Classroom3[0]).broadcast_address)-1)))

print(' ')
print('Classroom 4')
print('------------')
print('Classroom4 Network Address: {}'.format((Classroom3[1]).network_address))
print('Classroom4 Broadcast Address: {}'.format((Classroom3[1]).broadcast_address))
print('Classroom4 # of hosts: {}'.format(len(list((Classroom3[1]).hosts()))))
print('Classroom4 valid host range: {0} - {1}'.format((((Classroom3[1]).network_address)+1), (((Classroom3[1]).broadcast_address)-1)))

print(' ')
print('Classroom 5')
print('------------')
print('Classroom5 Network Address: {}'.format((Classroom4[0]).network_address))
print('Classroom5 Broadcast Address: {}'.format((Classroom4[0]).broadcast_address))
print('Classroom5 # of hosts: {}'.format(len(list((Classroom4[0]).hosts()))))
print('Classroom5 valid host range: {0} - {1}'.format((((Classroom4[0]).network_address)+1), (((Classroom4[0]).broadcast_address)-1)))

print(' ')
print('Classroom 1')
print('------------')
print('Classroom1 Network Address: {}'.format((classroom[0]).network_address))
print('Classroom1 Broadcast Address: {}'.format((classroom[0]).broadcast_address))
print('Classroom1 # of hosts: {}'.format(len(list((classroom[0]).hosts()))))
print('Classroom1 valid host range: {0} - {1}'.format((((classroom[0]).network_address)+1), (((classroom[0]).broadcast_address)-1)))

print(' ')
print('Classroom 2')
print('------------')
print('Classroom2 Network Address: {}'.format((classroom[1]).network_address))
print('Classroom2 Broadcast Address: {}'.format((classroom[1]).broadcast_address))
print('Classroom2 # of hosts: {}'.format(len(list((classroom[1]).hosts()))))
print('Classroom2 valid host range: {0} - {1}'.format((((classroom[1]).network_address)+1), (((classroom[1]).broadcast_address)-1)))