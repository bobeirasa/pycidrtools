__author__ = 'Rafael Lopes <dev@rafalopes>'

from Nets import *
from pieces import networklist

net = Nets(networklist)

net.printnetworks()
net.checkoverlaps()