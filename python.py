# # k = 10
# # n = 5

# # for i in range(n):
# #     print(k)

# for i in range(10):
#     print(i)

# scan_scapy.py
import socket
import ipaddress
from scapy.all import ARP, Ether, srp  # pip install scapy
import sys

def get_local_network_cidr(default_prefix=24):
    """Mahalliy IPni aniqlab, /24 tarmoqqa (agar aniq bo'lmasa) o'rnatadi."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except Exception as e:
        print("Local IP aniqlashda xato:", e)
        sys.exit(1)

    # Agar kerak bo'lsa, bu yerda tarmoq prefixini aniqlash uchun Qo'shimcha kod yozish mumkin.
    network = ipaddress.ip_network(f"{local_ip}/{default_prefix}", strict=False)
    return str(network)

def arp_scan(network_cidr, timeout=2):
    """Berilgan network CIRD bo'yicha ARP so'rovlari yuboradi va topilgan qurilmalarni qaytaradi."""
    arp = ARP(pdst=network_cidr)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # srp — layer 2 paketlarini yuboradi va javoblarni oladi.
    answered = srp(packet, timeout=timeout, verbose=False)[0]

    devices = []
    for sent, received in answered:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc,
            "who_has": sent.pdst
        })
    return devices

if __name__ == "__main__":
    print("Tarmoqni aniqlanmoqda...")
    net = get_local_network_cidr(default_prefix=24)
    print(f"Skanni boshlayapman: {net}  (admin/root huquqi talab qilinadi)")
    devices = arp_scan(net, timeout=2)

    if not devices:
        print("Hech qanday qurilma topilmadi. Root/administrator huquqi yoki tarmoq parametrlarini tekshiring.")
    else:
        print(f"Topilgan qurilmalar: {len(devices)}")
        print("{:16}    {:17}".format("IP manzil", "MAC manzil"))
        print("-"*36)
        for d in devices:
            print("{:16}    {:17}".format(d["ip"], d["mac"]))
