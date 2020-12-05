# Coded by @TrollSkull

import time, os, sys

loop = 1
ter = ""
ana = ()
edit = ()
edited = ()
text = ""

def ini():
	print(chr(27)+"[1;33m"+"""
(\ 
\\'\ 
\ \'\     __________  
 / '|   ()_________)
 \ '/    \ ~~~~~~~~ \\	    File
   \       \ ~~~~~~   \\	      Editor
  (==).      \__________\\
  (__)       ()__________)       Art by ?
""")

	print(chr(27)+"[1;37m"+"""____________________________________________""")

	print(chr(27)+"[1;37m"+"\n           Created by "+chr(27)+"[1;32m"+"@TrollSkull\n")

	print(chr(27)+"[1;30m"+"[INFO] Type \"show options\" to show command\n")
	
ini()

while (loop == 1):
	ter = str(input(chr(27)+"[1;0;37m"+"File "+chr(27)+"[1;33m"+">>"+chr(27)+"[1;37m"+" "))
	if ter == "show options":
		print(chr(27)+"[1;33m"+"""
      COMMAND                        DESCRIPTION"""+chr(27)+"[1;37m"+"""
  ---------------	-------------------------------------
   editor		 Edit files
   analyzer		 Parse any kind of file
   
   ls			 Muestra los archivos cercanos
   change log		 The list of changes in this version
   about		 Show information about this program
   clear		 Clean the terminal
   exit			 Exit the program\n""")
	elif ter == "exit":
			print(chr(27)+"[1;34m"+"\n["+chr(27)+"[1;31m"+"!"+chr(27)+"[1;34m"+"]"+chr(27)+"[1;37m"+" Exiting program\n")
			exit()
	elif ter == "change log":
		print(chr(27)+"[1;33m"+"\nChanges 1.1:\n")
		print(chr(27)+"[1;37m"+"""Added \"clear\" command
		
Change in program structure""")
		print(chr(27)+"[1;33m"+"\nChanges 1.2:")
		print(chr(27)+"[1;37m"+"""
Improvement when editing

Bug fixes""")
		print(chr(27)+"[1;33m"+"\nChanges 1.3:")
		print(chr(27)+"[1;37m"+"""
Added \"ls\" command

Bug fixes""")
		print(chr(27)+"[1;33m"+"\nChanges 1.4:")
		print(chr(27)+"[1;37m"+"""
Fixed the \"ls\" command error in Windows

Bug fixes
""")
	elif ter == "about":
		print(chr(27)+"[1;33m"+"""
   Author:"""+chr(27)+"[1;37m"+""" 	     	 TrollSkull
   """+chr(27)+"[1;33m"+"""Version:"""+chr(27)+"[1;37m"+"""   	 	 Alpha 1.4"""+chr(27)+"[1;33m"+"""
   Name:"""+chr(27)+"[1;37m"+"""		 Python File Editor"""+chr(27)+"[1;33m"+"""
   Contact:"""+chr(27)+"[1;37m"+"""		 trollskull.contact@gmail.com
   
   """+chr(27)+"[1;36m"+"""if you find any errors or problems, please contact author
""")
	elif ter == "clear":
		if sys.platform == "win32":
			os.system("cls")
			ini()
		else:
			os.system("clear")
			ini()
	elif ter == "analyzer":
			print(chr(27)+"[1;34m"+"\n["+chr(27)+"[1;32m"+"✓"+chr(27)+"[1;34m"+"]"+chr(27)+"[1;37m"+" Analyzer activated\n")
			print(chr(27)+"[1;30m"+"[INFO] Type the file to view\n")
			ana = input(chr(27)+"[1;0;37m"+"File/Analyzer "+chr(27)+"[1;33m"+">>"+chr(27)+"[1;37m"+" ")
			try:
				with open(ana) as f:
	 			   text = f.read()
			except FileNotFoundError: # Err (File)
				print(chr(27)+"[1;34m"+"\n["+chr(27)+"[1;31m"+"!"+chr(27)+"[1;34m"+"]"+chr(27)+"[1;37m"+" File not found")
			print(chr(27)+"[1;30m"+text)
			text = ""
	elif ter == "editor":
		print(chr(27)+"[1;34m"+"\n["+chr(27)+"[1;32m"+"✓"+chr(27)+"[1;34m"+"]"+chr(27)+"[1;37m"+" Editor activated\n")
		print(chr(27)+"[1;30m"+"[INFO] Type the file to edit or you can type\nthe name of a non-existent file to create it\n")
		edit = input(chr(27)+"[1;0;37m"+"File/Editor "+chr(27)+"[1;33m"+">>"+chr(27)+"[1;37m"+" ")
		if edit == "file-editor.py":
			print(chr(27)+"[1;30m"+"\n[INFO] No se puede editar este archivo\n")
		else:
			try:
				print(chr(27)+"[1;30m"+"\n[INFO] Type the new content\n")
				edited = input(chr(27)+"[1;0;37m"+"File/Editor/Text "+chr(27)+"[1;33m"+">>"+chr(27)+"[1;37m"+" ")
				with open(edit, "w") as f:
					f.write(edited)
				print(chr(27)+"[1;30m"+"\n[INFO] Successful file edited\n")
			except:
					print("")
	elif ter == "ls":
		if sys.platform == "win32":
			print(chr(27)+"[1;30m"+"\n[INFO] Archivos cercanos\n"+chr(27)+"[1;33m")
			os.system("dir /w")
			print("")
		else:
			print(chr(27)+"[1;30m"+"\n[INFO] Archivos cercanos\n"+chr(27)+"[1;33m")
			os.system("ls")
			print("")
	else:
		print(chr(27)+"[1;34m"+"\n["+chr(27)+"[1;31m"+"!"+chr(27)+"[1;34m"+"]"+chr(27)+"[1;37m"+" Command \"" + ter + "\" not found\n")
