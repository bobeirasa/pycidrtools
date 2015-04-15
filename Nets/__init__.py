__author__ = 'Rafael Lopes <dev@rafalopes.com.br>'

import ipaddr

class Nets:
    def __init__(self, networklist):
        self.CIDRList = []
        for x in networklist:
            self.CIDRList.append(ipaddr.IPNetwork(x))

    def checkoverlaps(self):
        for x in self.CIDRList:
            for y in self.CIDRList:
                if x.overlaps(y):
                    if x == y:
                        continue
                    print str(x) + " overlaps with " + str(y)

    def printnetworks(self):
        print "Listing all networks: "
        for x in self.CIDRList:
            print x
        print