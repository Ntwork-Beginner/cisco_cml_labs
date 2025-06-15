from netmiko import ConnectHandler

# Ask user for device details
ip = input("Enter router IP address :) ")
username = input("Enter SSH username :) ")
password = input("Enter SSH password :) ")
secret = input("Enter enable (secret) password :) ")

# Define the device with the inputs
router = {
    'device_type': 'cisco_ios',
    'host': ip,
    'username': username,
    'password': password,
    'secret': secret,
    }

# Define DHCP configuration commands
dhcp_config = [
    'ip dhcp excluded-address 172.16.1.1 172.16.1.10',
    'ip dhcp pool MYPOOL',
    'network 172.16.1.0 255.255.255.0',
    'default-router 172.16.1.1',
    'dns-server 8.8.8.8',
    ]

# Define HSRP configuration
hrsp_config = [
    'end',
    'en',
    'conf ter',
    'interface e0/1',
    'no shut',
    'standby 1 ip 172.16.1.1',
    ]

# Connect and enter enable mode
try:
    net_connect = ConnectHandler(**router)
    net_connect.enable()

    # Run the command and save output
    output = net_connect.send_command('show ip int br')
    print("\n Router Interfaces:\n")
    print(output)

     # Apply DHCP configuration
    dhcp_output = net_connect.send_config_set(dhcp_config)
    print("\n DHCP configuration applied :)")
    print(dhcp_output)

    # Apply HSRP configuration
    hsrp_output = net_connect.send_config_set(hsrp_config)
    pritn("\n HSRP configuration applied :)")
    print(hsrp_output)

    # Disconnect
    net_connect.disconnect()

except Exception as e:
    print(f"\n Connection failed: {e}")
