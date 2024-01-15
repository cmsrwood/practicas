import requests
from lxml import html

encabezado={
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

url= "https://mikiweys.github.io/dcalauncher/index.html"

respuesta=requests.get(url, headers=encabezado)

parser=html.fromstring(respuesta.text)

print (parser)

# español=parser.get_element_by_id("js-link-box-es");
# print(español.text_content())

español=parser.xpath("+//a[@id='js-link-box-es']/strong/text()")
print(español)