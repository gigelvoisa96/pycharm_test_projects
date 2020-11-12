import http.client
def getShopContent(domain, path):
    conn = http.client.HTTPSConnection("shop.one-it.ro")
    payload = "{}"
    conn.request("GET", "/gomag/", payload)
    res = conn.getresponse()
    data = res.read()
    return data
if __name__ == '__main__':
    data = getShopContent("shop.one-it.ro", "/gomag/")
    print(data.decode("utf-8"))
