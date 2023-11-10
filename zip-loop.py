#!/usr/bin/env python3
#!/usr/bin/python

#promo-vpn-5@india.tr0.png

from pathlib import Path
import os,sys

print(f'CREATE p_name№s_name.zip FROM ALL p_name№.s_name* FILES IN USING DIRECTORY')

f_path = input("Enter path to the directory containing files for zipping (press ENTER for use current directory): ")
if f_path =='':
    u_path = '.'
else:
    u_path = str(f_path)
os.chdir(u_path)    
print(f'Using directory: {os.getcwd()}')

p_name = input("Enter name (before №): ")
s_name = input("Enter second static part of name (after №) OPTIONAL (press ENTER if you have not it): ")
i = int(input("Enter first number (№): "))
n = int(input("Enter last number (№): "))


while i<=n:
    print(i)
    os.system(f'zip {p_name}{i}{s_name}.zip {p_name}{i}{s_name}*')
    i+=1

print(f'Ziping successfully completed! in directory: {os.getcwd()}')

