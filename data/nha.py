import requests
from bs4 import BeautifulSoup

proxy = {'http': 'http://221.132.18.26:8090'}

def nha():
    name_clb = []
    getdata = requests.get(
        "https://www.24h.com.vn/bong-da/bang-xep-hang-bong-da-anh-c48a466585.html", proxies= proxy
        )
    handle_data = BeautifulSoup(markup=getdata.text, features= "lxml")
    info_topfive = handle_data.find_all(name='div', attrs={'class': 'info-club'})
    for i in range(0, 10):
        clb_f = " ".join(info_topfive[i].text.split())
        name_clb.append(f"TOP{i + 1}: {clb_f}")
    result = '\n'.join(name_clb)
    return result