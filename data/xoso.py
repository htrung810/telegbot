from webbrowser import get
from bs4 import BeautifulSoup
import requests
import json
import argparse

#proxyvn
def get_xoso():
    proxy = {'http': 'http://221.132.18.26:8090'}
    linkget = requests.get("https://ketqua.vn/", proxies= proxy)
    tree = BeautifulSoup(markup= linkget.text, features= "lxml")
    data = tree.find(name="div", attrs={"class": "data-kqxs hidden"}).text
    result = json.loads(data)
    return result


def test(numbers):
    tester = get_xoso()
    good_luck = []
    result = ""
    for i in tester:
        for c in tester[i].split("-"):
            good_luck.append(c[-2:])
    for number in numbers:
        if str(number) in good_luck:
            result = "Ohhhhhh ze! you are so luck! 1.000.000.000$ is yours"
        else:
            result = "I'm sorry babe! Wish you luck next time"
    return result


def solve(numberz):
    result = test(numberz)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('yournumber', type=str, nargs='*')
    args = parser.parse_args()
    if args.yournumber == []:
        price = get_xoso()
        for i in price:
            if i == "g0":
                print(f"Giai Dac Biet: {price[i]}")
            else:
                print(i ,price[i])

    else:
        print(solve(args.yournumber))



if __name__ == "__main__":
    main()
