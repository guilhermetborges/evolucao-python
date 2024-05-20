import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('não foi possivel acessar o site')
else:
    print('foi possivel acessar o site!')
    print(site.read)