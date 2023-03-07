#!/usr/bin/python

#===========================================Menu================================================

def menu():
    print("[1] Creat a network")
    print("[2] Ping test")
    print("[3] Fail test")
    print("[0] Exit the program")
    
#--------------------------------------------------------------------------------------------   

def option1():
        print("Success to create a network with 2 hosts, 3 switches and a SDN controller")

        
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
            
#This script creates a topology with two hosts (h1 and h2), three switches (s1, s2, and s3), and a remote SDN controller. The hosts are connected to the switches in a way that creates two paths from h1 to h2, one through s1 and s2 and another through s1, s3, and s2. The script also starts the network, tests connectivity, and opens a CLI for interactive use. To run this script, save it as a Python file (e.g., sdn_topo.py) and run it using the command sudo python sdn_topo.py.
          
#--------------------------------------------------------------------------------------------        
        
def option2(net):
        # Send 100 ping packets from H1 to H2 via Path 1
        print("Sending 100 ping packets from H1 to H2 via Path 1")
        h1 = net.get('h1')
        h2 = net.get('h2')
        h1.cmd('ping -c 100', h2.IP(), '-I', h1.IP())
        
        # Send 100 ping packets from H1 to H2 via Path 2
        print("Sending 100 ping packets from H1 to H2 via Path 2")
        h1.cmd('ping -c 100', h2.IP(), '-I', '10.0.0.3')
        
#--------------------------------------------------------------------------------------------  

def option3(net):
        print("Link1 failed")
        # Make Link 1 fail
        link1 = net.linksBetween(net.get('h1'), net.get('s1'))[0]
        link1.linkDown()
          
        
#---------------------------------------------------------------------------------------  
        
        
menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        option1()
        #do option 1 stuff
        #print("option 1 has been called.")
    elif option == 2:
        option2()
        #do option 2 stuff
        #print("Option 2 has been called.")
    elif option == 3:
        option3()
        #do option 3 stuff
    else:
        print("Invalid option.")
    
    print()
    menu()
    option = int(input("Enter your option: "))
    
print("Thanks for using this program. Goodbye.")

#========================================================================================