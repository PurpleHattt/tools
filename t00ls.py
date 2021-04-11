import os 
import sys
import apt
from subprocess import run, PIPE
from colorama import Fore, Back, Style

os.system('sudo apt install toilet -y')

print(Fore.YELLOW)
print('-' * 50) 
print(Fore.GREEN)
print('            RECON.PY   ')
print("Made BY @PurpleHattt - Github")
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

os.system('systemctl enable --now snapd apparmor')



os.system('apt update; apt upgrade -y; apt install python3; apt install python3-pip; apt autoclean -y')
os.system("""sudo apt update;
sudo apt install curl gpg software-properties-common apt-transport-https; 
curl -sSL https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -; 
echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" | sudo tee /etc/apt/sources.list.d/vscode.list;
sudo apt update;
sudo apt install code
 """)

print(Fore.BLUE)
pycharm = (input("""1.Do you want to install pycharm: \n2.Pycharm Pro: \n3.No pycharm:\n
1.\n2.\n3.\n
"""))
if pycharm == "1":
    print("Installing Pycharm basic")
    os.system('sudo snap install pycharm-community --clasic')
elif pycharm == "2": 
    print('installing Pycharm Pro')
    os.system('sudo snap install pycharm-professional --classic')
elif pycharm == "3": 
    print('NOT installing pycharm')
print(Fore.RESET)
if pycharm == "1": 
    print("Pycharm basic")
elif pycharm == "2":
    print("Pycharm Pro")




print('T00ls installed: ' + str(ut_list))

i = (input("Do you want to reboot now? y/n:\n")) 
if i == "y": 
    os.system("sudo reboot")
elif i == "n": 
    print(Fore.RED)
    print("All tools are now installed, don't forget to reboot.")
    print("""                                                        
 mmmmmm          "      m      m      "                 
 #      m   m  mmm    mm#mm  mm#mm  mmm    m mm    mmmm 
 #mmmmm  #m#     #      #      #      #    #"  #  #" "# 
 #       m#m     #      #      #      #    #   #  #   # 
 #mmmmm m" "m  mm#mm    "mm    "mm  mm#mm  #   #  "#m"# 
                                                   m  # 
                                                    ""  
""")
    sys.exit 
    
