from xml.dom.minidom import Document, parse
import xpath


def addElementToTopElement(document, topElement, newElementName, newElementText):
    newElement = document.createElement(newElementName)
    topElement.appendChild(newElement)
    text = document.createTextNode(newElementText)
    newElement.appendChild(text)   


claudia = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCjpcWauPV2Kr/6DoskraJu4SCtXf454CQhN467hpPkGJtC3hrlahsf02nnF0b0nxg5tQWdEPAa1YT5eOknvspOot+AwoTzPWusflx1BCIDCiU0y2Yu98bbrD7aLAIqj8u2KkyjhQlt6nOB9MNMsFwTkwfwWCMvYv8zcD8BMDPAwQIDAQAB"
joao =  """-----BEGIN CERTIFICATE-----
MIIHFjCCBf6gAwIBAgIIQZhP2zb18CIwDQYJKoZIhvcNAQEFBQAwfDELMAkGA1UEBhMCUFQxHDAa
BgNVBAoME0NhcnTDo28gZGUgQ2lkYWTDo28xFDASBgNVBAsMC3N1YkVDRXN0YWRvMTkwNwYDVQQD
DDBFQyBkZSBBdXRlbnRpY2HDp8OjbyBkbyBDYXJ0w6NvIGRlIENpZGFkw6NvIDAwMDUwHhcNMTEx
MjI5MTExNDM2WhcNMTYxMjI5MDAwMDAwWjCB1DELMAkGA1UEBhMCUFQxHDAaBgNVBAoME0NhcnTD
o28gZGUgQ2lkYWTDo28xHDAaBgNVBAsME0NpZGFkw6NvIFBvcnR1Z3XDqnMxIzAhBgNVBAsMGkF1
dGVudGljYcOnw6NvIGRvIENpZGFkw6NvMRUwEwYDVQQEDAxTw4EgREEgU0lMVkExFDASBgNVBCoM
C0pPw4NPIFBBVUxPMRQwEgYDVQQFEwtCSTEzNzYwOTA5NDEhMB8GA1UEAwwYSk/Dg08gUEFVTE8g
U8OBIERBIFNJTFZBMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCrWoBZiayJ2oRv7B07f/uV
LbXxuvFUQAmgZO5k3kDPW7I0jzq+6+B/snzz3+jV4oWKdAg3cvnT4grA3f/vlzBLvXJy4bsx90Y3
clMbTImkLFJbmd1V8/zq2GVZLW3uQnuLlOFrPrmH0bUU6ABk3GTFbvEhLeX9LnCDMb7/IrWTiwID
AQABo4IDxTCCA8EwDAYDVR0TAQH/BAIwADAOBgNVHQ8BAf8EBAMCA4gwHQYDVR0OBBYEFOx8q+U9
G5+G8ofqD7rVEqOIqtWrMB8GA1UdIwQYMBaAFMu8aIu4gPEWNGRz5Yx1ebtckwlRMIIB9QYDVR0g
BIIB7DCCAegwgfIGCGCEbAEBAQIUMIHlMCgGCCsGAQUFBwIBFhxodHRwOi8vd3d3LnNjZWUuZ292
LnB0L3BjZXJ0MIG4BggrBgEFBQcCAjCBqx6BqABPACAAYwBlAHIAdABpAGYAaQBjAGEAZABvACAA
ZQBtAGkAdABpAGQAbwAgAHMAZQBnAHUAbgBkAG8AIABlAHMAdABhACAAcABvAGwA7QB0AGkAYwBh
ACAA6QAgAHUAdABpAGwAaQB6AGEAZABvACAAcABhAHIAYQAgAGEAdQB0AGUAbgB0AGkAYwBhAOcA
4wBvACAAZABvACAAQwBpAGQAYQBkAOMAbzB4BgtghGwBAQECBAIABzBpMGcGCCsGAQUFBwIBFlto
dHRwOi8vcGtpLmNhcnRhb2RlY2lkYWRhby5wdC9wdWJsaWNvL3BvbGl0aWNhcy9kcGMvY2Nfc3Vi
LWVjX2NpZGFkYW9fYXV0ZW50aWNhY2FvX2RwYy5odG1sMHcGDGCEbAEBAQIEAgABATBnMGUGCCsG
AQUFBwIBFllodHRwOi8vcGtpLmNhcnRhb2RlY2lkYWRhby5wdC9wdWJsaWNvL3BvbGl0aWNhcy9w
Yy9jY19zdWItZWNfY2lkYWRhb19hdXRlbnRpY2FjYW9fcGMuaHRtbDBrBgNVHR8EZDBiMGCgXqBc
hlpodHRwOi8vcGtpLmNhcnRhb2RlY2lkYWRhby5wdC9wdWJsaWNvL2xyYy9jY19zdWItZWNfY2lk
YWRhb19hdXRlbnRpY2FjYW9fY3JsMDAwNV9wMDAwNC5jcmwwcQYDVR0uBGowaDBmoGSgYoZgaHR0
cDovL3BraS5jYXJ0YW9kZWNpZGFkYW8ucHQvcHVibGljby9scmMvY2Nfc3ViLWVjX2NpZGFkYW9f
YXV0ZW50aWNhY2FvX2NybDAwMDVfZGVsdGFfcDAwMDQuY3JsMEsGCCsGAQUFBwEBBD8wPTA7Bggr
BgEFBQcwAYYvaHR0cDovL29jc3AuYXVjLmNhcnRhb2RlY2lkYWRhby5wdC9wdWJsaWNvL29jc3Aw
EQYJYIZIAYb4QgEBBAQDAgCgMCgGA1UdCQQhMB8wHQYIKwYBBQUHCQExERgPMTk5MDA4MjMxMjAw
MDBaMA0GCSqGSIb3DQEBBQUAA4IBAQCtduT6W5h/y1cb1ghHirUMo6PGOpkHAv3AWy2axus/cEKT
8ML8B3NWlg5lbxsj7hGAGbX7PumyODJw/rLhp7bwt17kOOy0EX3RpozPSVQ9sH0XN0p2hcczjkva
cT4lBUJjKjzAqS/cMzidsDt0mkzvHQ+F0aGYTwi5ep/BC5usjUklnky4AYi3J+HOwt1TpvezFIeA
OeSueTAxzpHLLQHETz55LgvwyLA8fWZYblYZGv8KA6iQyTkFC4NQW3aj+mucNmJrHDUC3BPb4MXf
CifVJPCCUorlRqlSp+hr6lDijZ0/Ru6xJuu9XTgMZvA1AYuMjy3m1EcFDAL6AK6XQZTj
-----END CERTIFICATE-----"""
    
    


doc = Document()
topElement = doc.createElement("users")
doc.appendChild(topElement)

newElement = doc.createElement("user")
topElement.appendChild(newElement)


addElementToTopElement(doc, newElement, "nBI", "137119453")
addElementToTopElement(doc, newElement, "certificate", claudia)

newElement = doc.createElement("user")
topElement.appendChild(newElement)

addElementToTopElement(doc, newElement, "nBI", "137609094")
addElementToTopElement(doc, newElement, "certificate", joao)


xmlFile = open("authorizedUsers.xml", "w")
doc.writexml(xmlFile)
xmlFile.close()



#creates the commands file
doc = Document()
topElement = doc.createElement("commandsLog")
doc.appendChild(topElement)
xmlFile = open("commandsLog.xml", "w")
doc.writexml(xmlFile)
xmlFile.close()

'''
doc = parse("commandsLog.xml")
print len(xpath.find("/commandsLog/user/session[../nBI/text()='" + "13711945" + "' and id/text()='" + "1" + "']", doc))
'''





