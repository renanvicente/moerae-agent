import apt
from socket import socket, AF_INET, SOCK_STREAM
from json import loads, dumps


def checkUpgrade():
  list_packages = []
  cache=apt.Cache()
  cache.update()
  cache.open(None)
  cache.upgrade()
  for pkg in cache.get_changes():
    list_packages.append(pkg.name)
  return list_packages

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


#packages = { 'hostname': hostname,
#             'ip':  ip,
#             'packages': list_packages }

#packages = {'packages': checkUpgrade() }
#print(packages)
#  sock.send(dumps(vhost_dict))

if __name__ == '__main__':
#  packages = {'packages': checkUpgrade() }
  print(send_data('urleater.ananke.com.br',8888))
