#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.node import OVSSwitch, RemoteController

class SDNTopo(Topo):
    "SDN network topology with two paths from H1 to H2"
    
    def build(self):
        # Add 2 hosts, h1 and h2
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        
        # Add 3 switches, s1, s2, and s3
        s1 = self.addSwitch('s1', cls=OVSSwitch)
        s2 = self.addSwitch('s2', cls=OVSSwitch)
        s3 = self.addSwitch('s3', cls=OVSSwitch)
        
        # Add links for each connection
        self.addLink(h1, s1, cls=TCLink)
        self.addLink(s1, s2, cls=TCLink)
        self.addLink(s2, h2, cls=TCLink)
        self.addLink(s1, s3, cls=TCLink)
        self.addLink(s3, s2, cls=TCLink)

if __name__ == '__main__':
    # Create a topology
    topo = SDNTopo()
    
    # Create a Mininet network
    net = Mininet(topo=topo, controller=lambda name: RemoteController(name, ip='127.0.0.1', port=6633), autoSetMacs=True)
    
    # Start the network
    net.start()
    
    # Test the connectivity
    net.pingAll()
    
    # Start with CLI
    CLI(net)
    
    # Stop the network
    net.stop()
