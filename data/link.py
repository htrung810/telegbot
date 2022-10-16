import data.xoso
import data.nha as nha
import data.reply as reply
import requests


def kqxs_mb():
    price = data.xoso.get_xoso()
    result_1 = []
    for i in price:
        if i == "g0":
            result_1.append(f"Giai Dac Biet: {price[i]}")
        else:
            a = f'{i}: {price[i]}'
            result_1.append(a)
    result = "\n".join(result_1)
    return result

## cat
def cat():
    c = requests.get("https://api.thecatapi.com/v1/images/search").json()
    for image in c:
        return image["url"]