# Linksys-Smart-WiFi-Information-Disclosure
* Linksys Smart Wi-fi X-JNAP-Action Sensitive Information Disclosure for EA8500 router and many others.
* Target: Various Linksys routers
* http://www.linksys.com/us/support-article?articleNum=156266

![nss.py](http://i.imgur.com/cmEKwlO.png)


On the Linux EA8500 series router and others there are a number of administrative actions that require very little authentication. This tool can be used to extract as much sensitive data from the Router as possible (without having to login). Here is a list of unlocked methods:
```python
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
```


# Installation
```bash
git clone https://github.com/zeropwn/Linksys-EA8500-Information-Disclosure
cd Linksys-EA8500-Information-Disclosure
chmod +x nss.py
```

# Vulnerable Devices
```
Model Number	Description	Vulnerable Firmware Versions (less than or equal to)	
E1200	Linksys E1200	1.0.04 (build 1)	2.0.11 (build 1)
E4200	Simultaneous Dual-Band Wireless-N Gigabit Router	1.0.06 (build 3)	2.1.41 (build 164606)
EA2700	Simultaneous Dual-Band Wireless-N Gigabit Router	1.1.40 (build 189581)	
EA2750	Simultaneous Dual-Band Wireless-N Gigabit Router	1.1.8 (build 184154)	
EA3500	Simultaneous Dual-Band Wireless-N Gigabit Router	1.1.40 (build 162464)	
EA4500	Simultaneous Dual-Band Wireless-N Gigabit Router	2.1.42 (build 183584)	3.1.7 (build 181919)
EA5800	Simultaneous Dual-Band Wireless-AC Gigabit Router	1.1.6.186296	
EA6100	Simultaneous Dual-Band Wireless-AC Gigabit Router	1.1.6 (build 181939)	
EA6200	Simultaneous Dual-Band Wireless-AC Gigabit Router	1.1.41 (build 188556)	
EA6300	Simultaneous Dual-Band Wireless-AC Gigabit Router	1.1.40 (build 184085)	
EA6350	Simultaneous Dual-Band Wireless-AC Gigabit Router	3.1.10.191322	
EA6400	Simultaneous Dual-Band Wireless-AC Gigabit Router	1.1.40 (build 184085)	
EA6500	Simultaneous Dual-Band Wireless-AC Gigabit Router	1.1.40 (build 176451)	
EA6700	Simultaneous Dual-Band Wireless-AC Gigabit Router	1.1.41 (build 183873)	
EA6900	Simultaneous Dual-Band Wireless-AC Gigabit Router	2.0.3.186963	1.1.43 (build 182871)
EA7300	Max-Stream AC1750 MU-MIMO GIGABIT ROUTER	1.1.4.192824	
EA7400	Simultaneous Dual-Band Wireless-AC Gigabit Router	2.0.7.191563	1.1.5.190349
EA7500	Max-Stream AC1900 MU-MIMO GIGABIT ROUTER	2.0.7.191563	1.1.5.190349
EA8100	Max-Stream AC2600 MU-MIMO GIGABIT ROUTER	1.0.2.193233	
EA8300	Linksys AC2200 MU-MIMO Gigabit Tri-Band Router	1.1.4.191539	
EA8500	Simultaneous Dual-Band Wireless-AC Gigabit Router	1.1.9.192968	
EA9200	Linksys AC3200 Tri-Band Smart Wi-Fi Router	1.1.9 (Build 183676)	
EA9300	Linksys MAX-STREAM AC4000 MU-MIMO Tri-Band Router	1.1.9.183697	
EA9400	Linksys MAX-STREAM AC5000 MU-MIMO Gigabit Router	1.0.3.181249	
EA9500	Linksys MAX-STREAM AC5400 MU-MIMO Gigabit Router	2.1.1.186574	1.1.7.180968
WRT1200AC	Simultaneous Dual-Band Wireless-AC Gigabit Router	2.0.6.191786	1.0.5.187766
WRT1900AC	Simultaneous Dual-Band Wireless-AC Gigabit Router	2.0.8.187766	1.1.10.187766
WRT1900ACS	Simultaneous Dual-Band Wireless-AC Gigabit Router	2.0.2.188405	1.0.3.187766
WRT3200ACM	Simultaneous Dual-Band Wireless-AC Gigabit Router	1.0.6.186168	
XAC1200	Simultaneous Dual-Band Wireless-AC Gigabit Router	1.1.42.166111	
XAC1900	Simultaneous Dual-Band Wireless-AC Gigabit Router	1.1.42.162280
WHW01	Velop	1.1.10.191690
WHW03	Velop	1.1.8.192419	2.1.8.192419
```
