# Steps for RMCCDC Firewall Configuration

## Secure Firewall

<span style="color:Lightgreen">Hypervisor Console</span>

<span style="color:Lightblue">PA3050 Console</span>

### 1. Connect to console
* Check Hyper terminal settings
  * Bits per sec : 9600
  * Data bits : 8
  * Parity : none
  * Stop bits : 1
  * Flow control : none
* If connecting through Linux run `sudo screen /dev/ttyUSB0 9600,cs8,-ixon,ixoff`
* To clear screen: `ctrl+L` 
### 2. Turn scripting off: `set cli scripting-mode off`
### 3. Enter configuration via `configure` command (same for both consoles).
### 4. <span style="color:Lightgreen"> Set device to 127.0.0.1 </span>
* `set deviceconfig system permitted-ip 127.0.0.1`
### 5. Temporarily disconnect from external data interfaces.
* `set network interface ethernet ethernet1/1 link-state down`
* `commit`
### 6. Change admin password
* `set mgt-config users admin password`
  * It is suggested to use an SSH key if possible.
### 7. Check system information: `show system info`
* You will need to change the management interface, so it has internet access.
  * It is defaulted to DHCP, that will need to be disabled before configuring static addresses.
* Check OS version and licenses.
### 8. Change management IP addr. if required.
* Notes for this step:
    * We are on a CIDR /24 subnet (i.e., 255.255.255.0).
    * Network topology will have the default-gateway listed.
* <span style="color:Lightblue">PA3050: `set deviceconfig system ip-address x.x.x.x netmask x.x.x.x default-gateway x.x.x.x dns-setting servers primary x.x.x.x`</span>
* <span style="color:Lightgreen">Hypervisor
    * Turn management console off first: `set deviceconfig system type static`
    * Change management IP addr: `set deviceconfig system ip-address x.x.x.x netmask x.x.x.x default-gateway x.x.x.x dns-setting servers primary x.x.x.x`
* `commit`
### 9. Restrict access to secure protocols.
* Check systems services `show system services`
* Verify any unneeded services (i.e., telnet)
* To disable a service, enter: `set deviceconfig system service disable-<selected service> no`
* To enable a service, enter: `set deviceconfig system service disable-<selected service> yes`
* `commit`
### 10. Restrict admin accounts
* Delete any admin account that is not admin or panorama
    * `show admins all`
    * `delete mgt-config users <account>`
      * repeat if needed
    * `commit`
### 11. turn interfaces back on.
* `set network interface ethernet ethernet1/1 link-state up`
* `commit`
### 12. Turn management console interface on
* <span style="color:orange">The permitted-ip should be listed on the network topology.</span>
* `set deviceconfig system permitted-ip x.x.x.x`
* `commit`
### 13. Export configuration to a secure location
* `scp export configuration to <location>`
---
## License Appliance
1. Login to PaloAlto interface
2. Go to <b>Device</b> tab
3. Select <b>Licenses</b>
4. Under <i>License Management</i> select <b>Retrieve license keys from license server</b>
5. Reboot system and then login again
6. Go to <b>Device</b> tab
7. Select <b>Licenses</b>
8. Verify the following licenses:
   1. AutoFocus Device License
   2. GlobalProtect Gateway
   3. PAN-DB URL Filtering
   4. Virtual Systems
   5. GlobalProtect Portal
   6. Threat Prevention
   7. WildFire License
9. <b>NOTE: There may be an expired license in the setup. That will not break the system.</b>
---
## Download Latest Software
1. Go to <b>Device</b>
2. Select <b>Dynamic Updates</b>
3. Click <b>Check Now</b>
4. Select <i>Download and Install</i> on all applicable tabs
5. Click <b>Check Now</b>
---
## Configure Network Deployment & Security Policies
### *The competition environment is most likely already configured to a Layer 2 or Layer 3 setup. The best practice is to verify that their configuration is what your team needs.*
---
## Turn On Full Firewall Functionality & Best Practices
### 1. Complete visibility of traffic
 * Have a list of allowed applications
   * Include any custom applications
 * SSL Decryption
 * User-ID
### 2. Reduce attack surface area
* Whitelist applications
* Create custom App-ID's
* Dynamic address lists and groups
* SSL Protocol Settings
### 3. Protect Against known attacks
* Assign security profiles to firewall via the security policies
  * Anti-virus profiling
    * Enable blocking by AV signature
    * Enable blocking by Wilffire signature
  * Vulnerability profile
  * Anti-Spyware
    * DNS beacon protection
    * Block by anti-spyware signature
  * File blocking
  * URL Filtering/C2 Websites
  * Protect against DoS, Reconnaissance Malformed Packets, Bad Protocols
    * Zone protection profile
    * DoS profile
    * Use <i>External Dynamic Lists</i> to block bad traffic
### 4. Protect against unknown attacks
* WildFire analysis
  * Unknown file analysis
  * 5 minute malware signature generation
### 5. Extend Firewall Protection
* Firewall Client VPNs
  * Client VPNs GlobalProtect
* Firewall Site-to-Site VPNs
  * Site-to-Site VPN
* Firewall logs and reports
  * Logs and reports
  * Monitoring and Reporting
* Hot standby back-up Firewall
  * Backup Firewall
  * Active/Passive High Availability


