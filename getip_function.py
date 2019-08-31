def get_mac(ip): #Esta funcion permite escanear una direccion IP y obtener su MAC
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request, timeout = 1, verbose = False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip":element[1].psrc, "mac":element[1].hwrc}
        clients_list.append(client_dict)
    return clients_list
