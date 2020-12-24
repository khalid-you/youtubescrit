from pafy import new

import colorama

colorama.init()

RED = '\u001b[31m'
CYAN = '\u001b[36m'
YELLOW = '\u001b[33m'

print(RED)

print("="*50, CYAN)

print("(Alpha Algorithms LLC)", RED)

print("="*50, YELLOW)

link = input("Please enter a link: ")

video = new(link)

stream = video.allstreams
print(RED)
for quality in stream:
    print(quality)

print(YELLOW)
user_input = int(input("Please chose a quality: "))

stream[user_input].download()

colorama.deinit()