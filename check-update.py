#!/usr/bin/env python

__version__ = '0.0.1'

import apt
from socket import socket, AF_INET, SOCK_STREAM
from json import loads, dumps


def checkUpgradeDebian():
  list_packages = []
  cache=apt.Cache()
  cache.update()
  cache.open(None)
  cache.upgrade()
  for pkg in cache.get_changes():
    list_packages.append(pkg.name)
  return list_packages

def checkUpgrade():
  return checkUpgradeDebian()

def send_data(server,server_port):
  sock = socket(AF_INET, SOCK_STREAM)
  sock.connect((server,server_port))
  ip = sock.getsockname()[0]
  packages = { 'ip':  ip,
               'packages': checkUpgrade() }
  sock.send(dumps(packages))
  result = loads(str(sock.recv(1024)))
  sock.close()
  return result

if __name__ == '__main__':
  server = '127.0.0.1'
  port   = 8888
  print(send_data(server,port))
