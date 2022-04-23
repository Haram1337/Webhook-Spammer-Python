import sys 
from dhooks import Webhook
from colorama import Fore


print(Fore.MAGENTA + """
░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗░ ██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝ ██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░ ╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░░ ╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗ ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝ ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
""")

print(Fore.MAGENTA + """
                                            ╔════════════════════════════╗
                                            ║    Made by : Haram#1337    ║
                                            ║════════════════════════════║
                                            ║   1. Set the Webhook       ║
                                            ║   2. Set the message       ║
                                            ╚════════════════════════════╝
""")

link = input(Fore.WHITE + "[" + Fore.RED + "-" + Fore.WHITE + "] Enter the Webhook link: ")
message = input(Fore.WHITE + "[" + Fore.RED + "-" + Fore.WHITE + "] Enter the message: ")
print(Fore.RESET + " ")

while True:
    print(Fore.WHITE + "[" + Fore.GREEN + "+" + Fore.WHITE + "] Sending: " + message)
    try:
        hook = Webhook(link)
        hook.send(message)
    except:
        print(Fore.RESET + " ")
        print(Fore.RED + "/!\ Something Happend \n/!\ Probably Broken Webhook -> " + Fore.LIGHTYELLOW_EX + link)
        exit()