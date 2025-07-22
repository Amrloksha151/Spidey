import requests
import threading
from bs4 import BeautifulSoup
import argparse
from math import floor
import art

##### Arg Parser #####
parser = argparse.ArgumentParser(
    prog="Spidey",
    description="A web crawling utiltiy that supports threading, deep digging, and cookies. Author: @Amrloksha151",
    epilog="For donation send usdt to this wallet bnb smart chain wallet: 0x9371BbCA1d1C0b40ea13e91b56fFE45c99541212",
)

parser.add_argument("-u", "--url", help="Target url", required=True)
parser.add_argument("-p", "--port", help="Custom Target port")
parser.add_argument("-c", "--cookie", help="Cookies to be used")
parser.add_argument("-t", "--threads", help="Number of threads", required=True)
parser.add_argument("-d", "--deep", help="Deep digging", action="store_true")
parser.add_argument("-o", "--output", help="Output file to save results")
# parser.add_argument("-l", "--layers", help="How deep the diggig should be", default=1)
##### Arg Parser #####

args = parser.parse_args()
results = []


def main():
    print(art.text2art("Spidey", "random"))
    if args.port:
        resp = requests.get(f"{args.url}:{args.port}", cookies=args.cookie)
    else:
        resp = requests.get(args.url, cookies=args.cookie)
    tree = BeautifulSoup(resp.text, "lxml")
    layer1 = []
    for link in tree.find_all("a"):
        layer1.append(link.get("href"))
    if args.deep:
        step = floor(len(layer1) / int(args.threads))
        for i in range(0, len(layer1), step):
            threading.Thread(target=dig, kwargs={"links": layer1[i : i + step]}).run()
    return layer1


def dig(links: list):  # (ln:int, links:list):
    result = []
    for link in links:
        if link is not None:
            if link.startswith("/"):
                if args.port:
                    target = args.url + args.port + link
                else:
                    target = args.url + link
                resp = requests.get(target)
                tree = BeautifulSoup(resp.text, "lxml")
                for link in tree.find_all("a"):
                    result.append(link.get("href"))
            elif args.url in link:
                resp = requests.get(link)
                tree = BeautifulSoup(resp.text, "lxml")
                for link in tree.find_all("a"):
                    result.append(link.get("href"))
    results.append(result)


if __name__ == "__main__":
    final = main()
    if args.deep:
        for thread in threading.enumerate():
            if thread is not threading.main_thread():
                thread.join()
        for res in results:
            final.extend(res)
    if args.output:
        with open(args.output, "w") as f:
            for res in final:
                f.write(res + "\n")
    else:
        print("Final Results:")
        for res in final:
            print(res)
    print(f"Total links found: {len(final)}")
    print("Done!")
    print("Thanks for using Spidey!")
    print(
        "For donation send usdt to this wallet bnb smart chain wallet: 0x9371BbCA1d1C0b40ea13e91b56fFE45c99541212"
    )
