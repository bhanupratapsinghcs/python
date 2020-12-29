import datetime
import os

os.chdir('E:\Data\Programs\python\python')

folders = os.listdir()


def createFile(folder, file_name):
    date = datetime.datetime.now()
    d_string = date.strftime('%a_%d_%b_%Y')
    file_name = file_name + '_' + d_string + '.py'
    with open(folder + '/' + file_name, 'w') as f:
        f.write('print("hello world")')


print("""Choose the folder
	'1. CodeChef'
	'2. CodeForce'
	'3. Hacker Rank'
	'4. kickStart'
	'5. My python Program'
	'6. Instagram'
	  """)
folder_number = int(input())

print('Enter file Name')
file_name = input()

if folder_number == 1:
    createFile(os.getcwd() + "/" + 'CodeChef', file_name)
elif folder_number == 2:
    createFile(os.getcwd() + "/" + 'codeForce', file_name)
elif folder_number == 3:
    createFile(os.getcwd() + "/" + 'Hacker Rank Python problems', file_name)
elif folder_number == 4:
    createFile(os.getcwd() + "/" + 'kick_Start', file_name)
elif folder_number == 5:
    createFile(os.getcwd() + "/" + 'my python programe', file_name)
elif folder_number == 6:
    createFile(os.getcwd() + "/" + 'python-instagram', file_name)
else:
    print('Choose correct option')
