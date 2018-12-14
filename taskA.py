import os
import sys
import numpy
from task9 import *

def main(args):
    cwd = Directory(os.getcwd())
    user_name = cwd.get_path_name().split('/')[2]
    while True:
        cmdtokens = input('{path}$ '.format(path=cwd.path)).split()
        if not cmdtokens:
            continue
        cmd = cmdtokens[0]
        cmdargs = cmdtokens[1:]

        if cmd == 'ls':
            print()
            path = cwd.path if not cmdargs else cmdargs[0]
            directory = cwd.getsubdirectory(path)
            for item in directory.items():
                if item.isfile():
                    print('{name}\tFILE\t{size}'.format(
                        name=item.getname(), size=len(item)))
                else:
                    print('{name}\tDIR'.format(name=item.getname()))
            print()
        
        elif cmd == 'cd':
            print()
            new_path = ''.join(cmdargs)
            if os.path.isdir(new_path):
                path = new_path
                if path.startswith('/'):
                    cwd = Directory(cwd.get_path_name() + path)
                    os.chdir(cwd.get_path_name())
                else:
                    if '../' in new_path :
                        for count in range(new_path.count('../')):
                            cwd = Directory(os.path.split(cwd.get_path_name())[0])
                            os.chdir(cwd.get_path_name())
                    else:
                        cwd = Directory(cwd.get_path_name() + '/' + path)
                        os.chdir(cwd.get_path_name())
            elif not cmdargs or cmdargs == ['~/']:
                path = '/home/' + user_name
                cwd = Directory(path)
                os.chdir(cwd.get_path_name())

            else:
                print('Error! There is no such directory!')

        elif cmd == 'cat':
            print()
            new_path = ''.join(cmdargs)
            if os.path.isfile(new_path):
                with open(new_path, 'r') as file:
                    for line in file:
                        print(line)
        
        elif cmd == 'head':
            number_of_rows = 10
            new_path = ''.join(cmdargs)
            if os.path.isfile(new_path):
                with open(new_path, 'r') as file:
                    while number_of_rows != 0:
                        print(file.readline())
                        number_of_rows -= 1
        
        elif cmd == 'tail':
            number_of_rows = 10
            new_path = ''.join(cmdargs)
            if os.path.isfile(new_path):
                with open(new_path, 'r') as file:
                     my_lines = file.readlines()
                     for line in my_lines[-number_of_rows:]:
                        print(line)
                        
        elif cmd == 'pwd':
            print(os.getcwd())
        elif cmd == 'touch':
            print()
            new_path = ''.join(cmdargs)
            File(new_path).create()            
        elif cmd == 'find':
            
        elif cmd == 'clear':
            print('\n' * 150)
        elif cmd == 'exit':
            print("Bye bye!")
            break
        else:
            print('Unknown command: {cmd}'.format(cmd=cmd))


if __name__ == '__main__':
    main(sys.argv)
