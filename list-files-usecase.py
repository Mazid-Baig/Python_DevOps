import os

folders = input('please enter the names of folders with spaces:').split()
# print(folders) use """code """ to comment out multiple lines

for folder in folders:
    print(folder)

    try:
      list_files = os.listdir(folder)
    except FileNotFoundError:
      print('file not found')
      break
    except PermissionError:
      print("permission denied, please elevate them")
      break
    print("listing files in the folder --" + folder)

for file in list_files:
  print(file)
