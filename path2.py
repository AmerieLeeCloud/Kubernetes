from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Create 2 hosts (h1, h2)
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        # Create 3 switches (s1, s2, s3)
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Create 5 links 
        self.addLink(h1, s1)
        self.addLink(s1, s2)
        self.addLink(s2, h2)
        self.addLink(s1, s3)
        self.addLink(s3, s2)

def runNetwork():
    topo = MyTopo()
    net = Mininet(topo=topo, switch=OVSSwitch, controller=Controller)
    net.start()
    h1, h2 = net.get('h1', 'h2')

    # Test path 2: H1-S1-S3-S2-H2
    info('*** Testing path 2: H1-S1-S3-S2-H2\n')
    net.configLinkStatus('s1', 's2', 'down')
    net.ping([h1, h2])
    
#==========================================================

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    runNetwork()
