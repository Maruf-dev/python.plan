# Boolean => bool
# if else elif => else if
# and or

usName = input("login ")
pwd = int(input('password '))

if usName == 'teamit' or pwd == 777:
  print(usName == 'teamit')
  print(pwd == 777)
  print('welcome to system')
else:
  print(usName == 'teamit')
  print(pwd == 777)
  print('error, try again')
