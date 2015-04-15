__author__ = 'Rafael Lopes <dev@rafalopes.com.br>'

from Nets import *
from pieces import networklist

net = Nets(networklist)

net.printnetworks()
net.checkoverlaps()