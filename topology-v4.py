import argparse

from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.node import Host, RemoteController
from mininet.topo import Topo
from stratum import StratumBmv2Switch

CPU_PORT = 255

class IPv4Host(Host):

    def config(self, mac=None, ip=None, defaultRoute=None, lo='up', gw=None,
               **_params):
        super(IPv4Host, self).config(mac, ip, defaultRoute, lo, **_params)
        self.cmd('ip -4 addr flush dev %s' % self.defaultIntf())
        self.cmd('ip -6 addr flush dev %s' % self.defaultIntf())
        self.cmd('ip -4 link set up %s' % self.defaultIntf())
        self.cmd('ip -4 addr add %s dev %s' % (ip, self.defaultIntf()))
        if gw:
            self.cmd('ip -4 route add default via %s' % gw)
        # Disable offload
        for attr in ["rx", "tx", "sg"]:
            cmd = "/sbin/ethtool --offload %s %s off" % (
                self.defaultIntf(), attr)
            self.cmd(cmd)

        def updateIP():
            return ip.split('/')[0]

        self.defaultIntf().updateIP = updateIP

class TutorialTopo(Topo):
    """Simple topology with one switch and two IPv4 hosts"""

    def __init__(self, *args, **kwargs):
        Topo.__init__(self, *args, **kwargs)

        # Single switch
        switch = self.addSwitch('s1', cls=StratumBmv2Switch, cpuport=CPU_PORT)

        # IPv4 hosts
        h1 = self.addHost('h1', cls=IPv4Host, mac="00:00:00:00:00:1A",
                           ip='172.16.1.1/24', gw='172.16.1.254')
        h2 = self.addHost('h2', cls=IPv4Host, mac="00:00:00:00:00:1B",
                           ip='172.16.1.2/24', gw='172.16.1.254')

        # Host links
        self.addLink(h1, switch)
        self.addLink(h2, switch)

def main():
    net = Mininet(topo=TutorialTopo(), controller=RemoteONOSController, ip="10.3.12.139", port=8181)
    net.start()
    CLI(net)
    net.stop()
    print '#' * 80

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Mininet topology script with one switch and two IPv4 hosts')
    args = parser.parse_args()
    setLogLevel('info')

    main()
