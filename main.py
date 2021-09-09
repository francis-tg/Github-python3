import getopt
import sys
import subprocess
from colorama import init
from colorama import Fore, Back, Style

repo_url = 'https://github.com/francis-tg/Github-python3.git'
spliturl = repo_url.split(".")
if spliturl[2] == "git":
    print('ok')



init()

# Get the arguments from the command-line except the filename
argv = sys.argv[1:]
sum = 0



if argv == ["-pull"]:
    print("Use to push data")
    try:
        gitadd = subprocess.check_output("git add .")
        print(gitadd)
        commit_msg = input("Entrer le message du commit >:")
        
        # Define the getopt parameters
        """ opts, args = getopt.getopt(argv, 'push:pull:', ['foperand', 'soperand']) """
        # Check if the options' length is 2 (can be enhanced)
        """ if len(opts) == 0 and len(opts) > 2:
        print ('usage: add.py -a <first_operand> -b <second_operand>')
        else:
        print(argv) """
        

    except getopt.GetoptError:
        # Print something useful
        print ('usage: add.py -a <first_operand> -b <second_operand>')
        sys.exit(2)
if argv == ["-push"]:
    print("Use to push data")
    try:
        commit_msg = input("Entrer le message du commit >:")
        gitadd = subprocess.run("git add .")
        gitadd = subprocess.run(f"git commit -m "+commit_msg+"")
        gitadd = subprocess.run("git push")

    except getopt.GetoptError:
        # Print something useful
        print ('usage: add.py -a <first_operand> -b <second_operand>')
        sys.exit(2)

if argv == ["-first-upload"]:
    print("Use to create respo")
    try:
        gitadd = subprocess.run("git init", shell=True, check=True)
        print("[+]"+Fore.GREEN+" Votre projet a été bien initialisé...")
        
        gitadd = subprocess.run("echo # Your project name >> README.md", shell=True, check=True)
        print("[+]"+Fore.GREEN+" Le README.md a été bien créé...")
        gitadd = subprocess.run("git add README.md", shell=True, check=True)
        print("[+]"+Fore.GREEN+" Le README.md a été bien ajouté...")
        commit_msg = input("Entrer le message du commit >:")
        gitadd = subprocess.run(f"git commit -m '"+commit_msg+"'", shell=True, check=True)
        print("[+]"+Fore.GREEN+" Le README.md a été bien ajouté...")
        gitadd = subprocess.run(f"git branch -M main", shell=True, check=True)
        repo_url= input("Entrer le lien de repository >:")
        spliturl = repo_url.split(".")
        if spliturl[2] == "git":
          gitadd = subprocess.run(f"git remote add origin {repo_url}", shell=True, check=True)
          subprocess.run('git push -u origin main', shell=True,check=True)
          pass
        else:
            print("[-]"+Fore.RED+" Le lien du repository n'est pas valid...")
            exit
        
        
        

        
        # Define the getopt parameters
        """ opts, args = getopt.getopt(argv, 'push:pull:', ['foperand', 'soperand']) """
        # Check if the options' length is 2 (can be enhanced)
        """ if len(opts) == 0 and len(opts) > 2:
        print ('usage: add.py -a <first_operand> -b <second_operand>')
        else:
        print(argv) """
        

    except getopt.GetoptError:
        # Print something useful
        print ('usage: add.py -a <first_operand> -b <second_operand>')
        sys.exit(2)