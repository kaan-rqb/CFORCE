import os
import time
import sys
import subprocess
from termcolor import colored

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    print(colored(r"""
   _____ ______ ____  _____   _____ ______ 
  / ____|  ____/ __ \|  __ \ / ____|  ____|
 | |    | |__ | |  | | |__) | |    | |__   
 | |    |  __|| |  | |  _  /| |    |  __|  
 | |____| |   | |__| | | \ \| |____| |____ 
  \_____|_|    \____/|_|  \_\\_____|______|
                                           
                                           
    """, "cyan"))
    print(colored("        by CyberForceTeam | Otomatik Araç Yöneticisi\n", "green", attrs=["bold"]))

def install_module(module):
    try:
        __import__(module)
    except ImportError:
        print(colored(f"📦 '{module}' modülü kuruluyor...", "yellow"))
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])

def clone_repo(repo_url, folder_name):
    if not os.path.exists(folder_name):
        print(colored(f"📥 '{folder_name}' klasörü bulunamadı, indiriliyor...", "cyan"))
        ret = os.system(f"git clone {repo_url} {folder_name}")
        if ret != 0:
            print(colored(f"❌ '{folder_name}' indirilemedi!", "red"))
            return False
        print(colored(f"✅ '{folder_name}' başarıyla indirildi.", "green"))
    else:
        print(colored(f"📂 '{folder_name}' zaten mevcut.", "blue"))
    return True

def run_script(folder_name, script_name, requirements=[]):
    for mod in requirements:
        install_module(mod)

    script_path = os.path.join(folder_name, script_name)
    if not os.path.exists(script_path):
        print(colored(f"❌ '{script_name}' dosyası '{folder_name}' içinde yok!", "red"))
        return

    print(colored(f"▶️ '{script_name}' çalıştırılıyor...\n", "green"))
    time.sleep(1)
    os.system(f"python3 {script_path}")

def main():
    install_module("termcolor")  # Bu aracı çalıştıran sistemde termcolor yoksa kurar
    while True:
        banner()
        print(colored("1) CyberRecon", "yellow"))
        print(colored("2) CYBERFORCESMSTOOL", "yellow"))
        print(colored("3) ForceSploit", "yellow"))
        print(colored("4) Çıkış", "red"))
        choice = input(colored("\nSeçiminiz: ", "green"))

        if choice == "1":
            if clone_repo("https://github.com/kaan-rqb/CyberRecon.git", "CyberRecon"):
                run_script("CyberRecon", "ForceReconNOW.py", ["requests", "termcolor"])

        elif choice == "2":
            if clone_repo("https://github.com/kaan-rqb/CYBERFORCESMSTOOL.git", "CYBERFORCESMSTOOL"):
                run_script("CYBERFORCESMSTOOL", "force.py", ["requests", "termcolor"])

        elif choice == "3":
            if clone_repo("https://github.com/kaan-rqb/ForceSploit.git", "ForceSploit"):
                run_script("ForceSploit", "ForceSploit.py", ["requests", "termcolor"])

        elif choice == "4":
            print(colored("Çıkış yapılıyor...", "red"))
            break

        else:
            print(colored("❌ Geçersiz seçim!", "red"))
            time.sleep(1)

if __name__ == "__main__":
    main()
