#!/bin/python3
import time
from time import sleep
import signal
import sys
import os
from rich.console import Console
from rich.progress import track
from rich.progress import Progress
from time import gmtime, strftime
from rich.table import Table
import shutil
import getpass
import platform
import subprocess
import urllib.request
import random



columns = shutil.get_terminal_size().columns
console = Console()
ltime = strftime("%a, %d %b %Y %H:%M:%S  " , gmtime())
user = getpass.getuser()
tries = 0 


def uptime():
 
     try:
         f = open( "/proc/uptime" )
         contents = f.read().split()
         f.close()
     except:
        return "Cannot open uptime file: /proc/uptime"
 
     total_seconds = float(contents[0])
 
     # Helper vars:
     MINUTE  = 60
     HOUR    = MINUTE * 60
     DAY     = HOUR * 24
 
     # Get the days, hours, etc:
     days    = int( total_seconds / DAY )
     hours   = int( ( total_seconds % DAY ) / HOUR )
     minutes = int( ( total_seconds % HOUR ) / MINUTE )
     seconds = int( total_seconds % MINUTE )
 
     # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
     string = ""
     if days > 0:
         string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
     if len(string) > 0 or hours > 0:
         string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
     if len(string) > 0 or minutes > 0:
         string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
     string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
 
     return string;
class system_obtain_file :
     def __init__(self):
         pass
     def processors():
         with open("/proc/cpuinfo", "r")  as f:
             info = f.readlines()
             cpuinfo = [x.strip().split(":")[1] for x in info if "model name"  in x]
             for index, item in enumerate(cpuinfo): 
                 processors = item.strip()
                 return processors
     def  architecture() :
      arch =  platform.architecture()[0] 
      return arch
    
     def machine():
      machine = platform.machine()
      return machine
    
     def node():
      node = platform.node()
      return node

     def system_os():
         system_os = platform.system()
         return system_os
        
     def connect():
         try : 
             urllib.request.urlopen('http://google.com') 
             return True
         except:
             return False   
class attempts :
    def __init__(self):
        pass


    def random_msg():
        clear = os.system("clear")
        num = random.randint(0,3)
        if num == 0 :
            clear
            print("DON'T DO IT AGAIN !")
        if num == 1 :
            clear
            print("rm -rf *  ? (y/n)")
        if num == 2 :
            clear
            while True :
                try :
                    print("\t\t\t\t###### WIPING ALL DATA ######")
                    attempts.spin()
                    break
                except :
                      break
        if num == 3 :
            clear
            console.print("Security over-riding attempt has been detected".center(columns),style="red")
            attempts.spin_1()
    def spin(): 
        with Progress() as progress:
            task = progress.add_task("Deleting system Files ", total=10)
            for job in range(10):
                attempts.do_step(job)
                progress.advance(task)
    def spin_1(): 
        try :
            with Progress() as progress:
                task1 = progress.add_task("[red]ERASING USER DATA ...", total=100)
                task2 = progress.add_task("[red]ERASING SYSTEM FILE...", total=100)
                task3 = progress.add_task("[red]ERASING CRITICAL DATA ", total=100)
                while not progress.finished:
                    progress.update(task1, advance=0.5)
                    progress.update(task2, advance=0.3)
                    progress.update(task3, advance=0.9)
                    time.sleep(0.02)
        except : 
            pass

    def do_step(self):
        for i in range (0,10) :
            sleep(0.1)
def system_info():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    console.print("System informations : ".center(columns),style="green")
    table = Table(  show_header=True, header_style="bold green")
    table.add_column("Architecture", style="dim", width=12)
    table.add_column("Processors ")
    table.add_column("Computer name ", justify="right")
    table.add_column("System ", justify="right")
    table.add_row(system_obtain_file.architecture(),system_obtain_file.processors() ,system_obtain_file.node(),system_obtain_file.system_os())
    table.add_row(system_obtain_file.machine())
    table.add_row()
    console.print(table,justify="center",style="green")
    print()
    system_obtain_file.connect()
    online_data = "System is Online External IP : " + external_ip  if system_obtain_file.connect() else "System is Offline"
    console.print(online_data.center(columns), style="green")    
def login_main():
    login_call = subprocess.run( "su $USER -c exit",stderr=subprocess.DEVNULL  ,shell=True)
    if login_call.returncode != 0 :
        try:
            failed_attempts()
        except :
            pass
        else:
            quit()
    else:
        print("Welcome Back")

        

def failed_attempts():
    global tries
    if tries == 0 :
        #tries += 1
        os.system("clear")
        console.print("ACCESS DENIED".center(columns), style="red")
        msg_1 = "Failed Attempts : "+ str(tries)
        console.print(msg_1.center(columns), style="red")
        sleep(2)
        main()
def main():
    os.system("clear")
    welcome = "[ " + str(ltime)+ "-  Logged User-Name : " + user + " ]"
    console.print(welcome.center(columns),style="green")
    up_time = "[      System is up since   : " + uptime() + "    ]" 
    console.print(up_time.center(columns),style="green")
    line = ('_' * 60 )
    console.print(line.center(columns),style="green")
    system_info()
    console.print("The terminal is locked ,  Please Enter your password >>>".center(columns) , style="green")
    while  True :
        try:
            login_main()
        except :
            attempts.random_msg()
        else:
            quit()
        

main()