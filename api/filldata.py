from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'http://localhost/Hackathon/noConvencioanles.php'

post_fields = {
    'direccion': 'direccion',
    'sertificaciones':'sertificaciones',
    'noClientes':'noClientes',
    'noClientesEsperados':'noClientesEsperados',
    'costoAdquisicionClientes':'costoAdquisicionClientes',
    'landinfPage':'landinfPage',
    'domainAge':'domainAge',
    'BBVA':'BBVA'
    }


request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()
print(json)