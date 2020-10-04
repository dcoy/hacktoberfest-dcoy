# Leonardo Zanotti

import sys,os,platform

args = sys.argv
extensions = ['md','pdf','html','txt']

##### colors
colors = True	# output colored c:
machine = sys.platform 		# detecting the os
checkPlatform = platform.platform()	# get current version of os
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
	colors = False 	# Mac and Windows shouldn't display colors :c
if checkPlatform.startswith("Windows-10") and int(platform.version().split(".")[2]) >= 10586:
	color = True	# coooolorssss \o/
	os.system('')	# Enables the ANSI -> standard encoding that reads that colors
if not colors:
	BGreen = BYellow = BPurple = BCyan = Yellow = Green = Red = Blue = On_Black = ''
else:
	BGreen = "\033[1;32m"     # Bold Green
	BYellow = "\033[1;33m"    # Bold Yellow
	BPurple = "\033[1;35m"    # Bold Purple
	BCyan = "\033[1;36m"      # Bold Cyan
	Yellow = "\033[0;33m"     # Yellow
	Green = "\033[0;32m"      # Green
	Red = "\033[0;31m"      # Red
	Blue = "\033[0;34m"     # Blue

	# Background
	On_Black="\033[40m"       # Black Background

##### logo
if len(args) != 3:		### Made with figlet or toilet
	print('''
		{BPurple}
\t                                                      ▄▄▄▄  
\t                                                     ██▀▀▀  
\t ████████   ▄█████▄  ████▄██▄   ▄█████▄   ██▄████  ███████  
\t     ▄█▀    ▀ ▄▄▄██  ██ ██ ██   ▀ ▄▄▄██   ██▀        ██     
\t   ▄█▀     ▄██▀▀▀██  ██ ██ ██  ▄██▀▀▀██   ██         ██     
\t ▄██▄▄▄▄▄  ██▄▄▄███  ██ ██ ██  ██▄▄▄███   ██         ██     
\t ▀▀▀▀▀▀▀▀   ▀▀▀▀ ▀▀  ▀▀ ▀▀ ▀▀   ▀▀▀▀ ▀▀   ▀▀         ▀▀   
		{BYellow} # Zanotti's markdown to pdf conversor{Blue}
		https://github.com/LeonardoZanotti/zamarf

To convert your file to another file type:
\t
{BGreen}$ python3 zabage.py file1.extension1 file2.extension2          
		'''.format(BPurple=BPurple,BGreen=BGreen,Blue=Blue,BYellow=BYellow,On_Black=On_Black))                                   

	sys.exit()
else:
	file1 = args[1]
	file2 = args[2]
	file1ext = file1.split('.')[1]
	file2ext = file2.split('.')[1]
	if (file1ext in extensions) and (file2ext in extensions):
		if (file1ext == 'pdf') and (file2ext == 'md'):
			os.system('pdf2md {file1}'.format(file1=file1))
		elif (file1ext != 'pdf'):
			os.system('pandoc {file1} -o {file2}'.format(file1=file1,file2=file2))
		else:
			print('I can\'t do this')
	else:
		print('Extension not permitted! Use one of the following: .md, .pdf, .html, .txt')