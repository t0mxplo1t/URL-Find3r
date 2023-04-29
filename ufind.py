import bs4,requests,os,argparse,time,sys

from bs4 import BeautifulSoup
from time import sleep
from argparse import ArgumentParser

def banner():
	print("""\033[32m
$$\   $$\ $$$$$$$\  $$\         $$$$$$$$\ $$\                 $$\  $$$$$$\ 
$$ |  $$ |$$  __$$\ $$ |        $$  _____|\__|                $$ |$$ ___$$\ 
$$ |  $$ |$$ |  $$ |$$ |        $$ |      $$\ $$$$$$$\   $$$$$$$ |\_/   $$ | $$$$$$\ 
$$ |  $$ |$$$$$$$  |$$ |$$$$$$\ $$$$$\    $$ |$$  __$$\ $$  __$$ |  $$$$$ / $$  __$$\ 
$$ |  $$ |$$  __$$< $$ |\______|$$  __|   $$ |$$ |  $$ |$$ /  $$ |  \___$$\ $$ |  \__|
$$ |  $$ |$$ |  $$ |$$ |        $$ |      $$ |$$ |  $$ |$$ |  $$ |$$\   $$ |$$ |
\$$$$$$  |$$ |  $$ |$$$$$$$$\   $$ |      $$ |$$ |  $$ |\$$$$$$$ |\$$$$$$  |$$ |
 \______/ \__|  \__|\________|  \__|      \__|\__|  \__| \_______| \______/ \__|\033[0m

\033[41m Simple URL Finder in Web Pages \033[0m\n\033[33m""")

def banner_2():
	print("""\033[36m
╦ ╦╦═╗╦   ╔═╗┬┌┐┌┌┬┐┬─┐
║ ║╠╦╝║───╠╣ ││││ ││├┬┘
╚═╝╩╚═╩═╝ ╚  ┴┘└┘─┴┘┴└─\033[0m""")

parser = ArgumentParser(description=banner_2())
parser.add_argument("-u","--url",help="http://example.com",required=True)

if len(sys.argv) == 1:
	parser.print_help()
	parser.exit()

if len(sys.argv) >= 1:
	os.system("clear")
	try:
		url = sys.argv[2]
		get = requests.get(url)
		find = BeautifulSoup(get.text,"html.parser")
		x = find.find_all("a")
		banner()
		for y in x:
			print(y.get("href"))
			sleep(0.2)

	except KeyboardInterrupt:
		print("Thanks for using URL-Find3r")
