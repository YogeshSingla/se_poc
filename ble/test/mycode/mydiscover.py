#script to connect to a specified BLE device and discover running services and their values

from bluepy import btle

DEVICE_MAC_ID = "38:A4:ED:CC:85:BE"		#yogesh's Mi MAX

#connect to device
print("Trying to connect to {}".format(DEVICE_MAC_ID))
dev = btle.Peripheral(DEVICE_MAC_ID)

#find services
print("Finding services ...")
for svc in dev.services:
	print str(svc)


	
#svc_uuid = btle.UUID("181C")
#service = dev.getServiceByUUID(svc_uuid)

#for ch in service.getCharacteristics():
	#print str(ch)
	#val = ch.read()
	#print("Properties: " + ch.propertiesToString())
	#print("Old Value: " + val)
	#ch.write("C")
	#print("New Value: " + ch.read())
	
	
	

