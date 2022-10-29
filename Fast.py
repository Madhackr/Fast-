import os
import time
import sys

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
        
        
os.system("clear")

print('''\033[91m
           __  __           _   _   _            _
          |  \/  | __ _  __| | | | | | __ _  ___| | ___ __
          | |\/| |/ _` |/ _` | | |_| |/ _` |/ __| |/ / '__|
          | |  | | (_| | (_| | |  _  | (_| | (__|   <| |
          |_|  |_|\__,_|\__,_| |_| |_|\__,_|\___|_|\_\_|
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

print('''\033[95m
            +--------------------------------------+
            | This Tool Install All Basic Packages |
            +--------------------------------------+
            | Coded By Mad Hackr | version :  2.0  |
            +--------------------------------------+''')




os.system ("apt update")
os.system ("atp upgrade -y")
os.system ("pkg install python -y")
os.system ("pkg install php -y")
os.system ("pkg install wget -y")
os.system ("git clone https://github.com/Bhai4You/Termux-Banner")

os.system ("git clone https://github.com/rixon-cochi/SMF.git")

