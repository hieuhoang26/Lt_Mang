import ipaddress as ip

CLASS_C = '192.168.0.0'
prefix = 25#24-30

if __name__ == '__main__':
    net_addr = CLASS_C + '/' + str(prefix)
    print("netword address: %s"%net_addr)
    try:
        network = ip.ip_network(net_addr)
    except:
        raise Exception("Fail to create network")
    print("network configuration\n")
    print("\t network address: %s"%network.network_address)
    print("number of IP address %s"%network.num_addresses)
    print("\t netmask: %s"%network.netmask)
    print("\t broadcast: %s"%network.broadcast_address)
    fist_ip, last_ip = list(network.hosts()) [0], list(network.hosts())[-1]
    print("\t host IP from %s to %s"%(fist_ip, last_ip))


# 192.168.0.0, subnet mask: 255.255.255.0
# 192.168.0.0/24, 192.168.0.0/26 -> 4 subnets, moi subnet co 64
# subnet mask: 255.255.255.192, xác định địa chỉ đầu, địa chỉ cuối, broadcast
# import ipaddress
# if __name__ == '__main__':
#     ip_addr = '192.168.0.0'
#     c = int(input("Nhap so bit (24-30):"))
#     net = ip_addr + '/' + str(c)
#     print("network address %s" % net)
#     network = ipaddress.ip_network(net)
#     # subnet mask mới
#     print("subnet mask: %s" % str(network.netmask))
#     dcdau = list(network.hosts())[0]
#     dccuoi = list(network.hosts())[-1]  # cuối cùng
#     print("dia chi dau %s, dia chi cuoi %s" % (dcdau, dccuoi))
#     # broadcast
#     print("broadcast %s" % str(network.broadcast_address))
