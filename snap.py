import os 
from subprocess import run, PIPE
from colorama import Fore 

os.system('sudo apt install toilet -y')

print(Fore.YELLOW)
print('-' * 50) 
print(Fore.CYAN)
os.system('toilet tools.py')
print(Fore.YELLOW)
print('-' * 50)
print(Fore.RESET)

def is_utility_inst(utility: str):
    application = run(f'apt-cache policy {utility}', shell=True, stdout=PIPE, stderr=PIPE, check=True)
    if 'none' in application.stdout.decode('utf-8'):
        try:
            os.system(f"sudo apt install {utility}")
        except:
            return False
    else: 
        pass
    return True


ut_list = ['nmap', 'nikto', 'gobuster', 'sublist3r', 'python3-pip', 'dirb', 'whatweb', 'toilet', 'vim', 'snapd',]
for ut in ut_list:
    is_utility_inst(ut)
