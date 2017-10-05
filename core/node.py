import socket
import urllib.request

class node(object):

  def __init__(self):
    self.ip = '127.0.0.1'
    self.port = 5001

  def get_local_ip(self):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
      # doesn't have to be reachable
      s.connect(('10.255.255.255', 1))
      IP = s.getsockname()[0]
    except:
      IP = '127.0.0.1'
    finally:
      s.close()

    return IP

  def get_external_ip(self):
    try:
      ip = urllib.request.urlopen('http://ident.me').read().decode('utf8')
      if ip != '':
        return ip
    except:
      pass
    
    return self.get_local_ip()


