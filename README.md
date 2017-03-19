# Linksys-EA8500-Information-Disclosure
* Linksys Smart Wi-fi X-JNAP-Action Sensitive Information Disclosure for EA8500 router and potentially others.
* Target: Linksys EA8500 router
* Firmware Version: 1.1.5.178908
* f/w Date: February 17th, 2017
* http://www.linksys.com/us/support-article?articleNum=156266

On the Linux EA8500 series router there are a number of administrative actions that require very little authentication. This tool can be used to extract as much sensitive data from the Router as possible (without having to login). Here is a list of unlocked methods:
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

![nss.py](http://i.imgur.com/cmEKwlO.png)


# Installation
```bash
git clone https://github.com/zeropwn/Linksys-EA8500-Information-Disclosure
cd Linksys-EA8500-Information-Disclosure
chmod +x nss.py
```
