from scapy.all import ARP, sniff, wrpcap





def sniffer_packet(packet):
    if (packet[ARP].op == 1):
        print("pedido: do endereco {} para o endereco {}".format(
            packet[ARP].psrc, packet[ARP].pdst
        ))
    elif (packet[ARP].op == 2):
        print("resposta: do mac {} para o endereco {}".format(packet[ARP].hwsrc,
         packet[ARP].pdst))
    print(packet.show())
data =  sniff(filter='arp', prn=sniffer_packet,  count=10)
wrpcap('data_sniffed.pcap', data)
    