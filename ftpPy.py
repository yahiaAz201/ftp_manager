from ftplib import FTP
import sys


host = input('Enter Your Host : ')
user = input('Enter Your Username : ')
password = input('Enter Your Password : ')



ftp = FTP(host)
ftp.login(user, password)
if ftp.getwelcome()[0:3] == '220' :
	print()
	print('Welcome you loged in FTP')
	print()

else :
	print()
	print(f'Password incorrcet please try again') 
	print()


def help(param):
	print("""  
	cd || cd file_name      'show files inside the server or navigate between' 
	ls                      'list files'
	upload file_name        'upload a file to the server'
	download file_name      'download a file from the server'
	exit                    'to exit from the script'
	""")
	param = param

help("")
	


def cd(param):
	
	path = param if param else "/"

	ftp.cwd(path or ftp.pwd()+path)	
	
	print()

def ls(param):
	for file in ftp.nlst():
		print()
		print(file)
		print("#".center(len(file),"#"))

def upload(param):
	
	full_path = param if param[0] != '/' else param[1:]
	filename = full_path.split('/')[-1]
	with open(full_path, "rb") as file:
   		ftp.storbinary(f"STOR {filename}", file)




def download(param):

	full_path = param if param[0] != '/' else param[1:]
	filename = full_path.split('/')[-1]
	with open(full_path, "wb") as file:
         ftp.retrbinary(f"RETR {filename}", file.write)


def exit(param):
	print('\033[32m' + 'Bye Bye :)')
	sys.exit()




while True:

	choice = input('\033[33m'+f'{ftp.pwd()}#>> '+'\033[m')
	
	func, *param = choice.split(' ')
	param = param[0] if param else False
	if func not in ["cd","upload","download","exit","help","ls"]: print('\033[31m' + f'Command {func} not found '+'\033[m')
	else : eval(func)((param))
	
		




	