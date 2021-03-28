import iptools

IP_LIST = iptools.IpRangeList("188.165.0.0/32")

if __name__ == '__main__':
    ips = IP_LIST.__iter__()
    while True:
        try:
            ip = iptools.next(ips)
            print(ip)
        except StopIteration:
            print("All send to scanner !")
            break
