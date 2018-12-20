import os
import sys
import numpy
import shutil
from task9 import *
from pathlib import Path

def main(args):
    cwd = Directory(os.getcwd())
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
            new_path = ''.join(cmdargs)
            if os.path.isdir(new_path):
                path = new_path
                if '..' in new_path :
                    for count in range(new_path.count('..')):
                        cwd = Directory(os.path.split(cwd.get_path_name())[0])
                        os.chdir(cwd.get_path_name())
                else:
                    cwd = Directory(os.path.join(cwd.get_path_name(), path))
                    os.chdir(cwd.get_path_name())
            elif not cmdargs or cmdargs == ['~/']:
                path = str(Path.home())
                cwd = Directory(path)
                os.chdir(cwd.get_path_name())
            else:
                print('Error! There is no such directory!')
        elif cmd == 'cat':
            new_path = ''.join(cmdargs)
            if os.path.isfile(new_path):
                with open(new_path, 'r') as file:
                    for line in file:
                        print(line.rstrip())
        elif cmd == 'head':
            number_of_rows = 10
            new_path = ''.join(cmdargs)
            if os.path.isfile(new_path):
                with open(new_path, 'r') as file:
                    while number_of_rows != 0:
                        print(file.readline().rstrip())
                        number_of_rows -= 1
        elif cmd == 'tail':
            number_of_rows = 10
            new_path = ''.join(cmdargs)
            if os.path.isfile(new_path):
                with open(new_path, 'r') as file:
                     my_lines = file.readlines()
                     for line in my_lines[-number_of_rows:]:
                        print(line.rstrip())
        elif cmd == 'pwd':
            print(os.getcwd())
        elif cmd == 'touch':
            new_path = ''.join(cmdargs)
            File(new_path).create()            
        elif cmd == 'find':
            find_file = ''.join(cmdargs)
            all_paths = list(map(lambda x: x.get_path_name(), Directory(os.getcwd()).filesrecursive()))
            for path in all_paths:
                if find_file in os.path.split(path)[1]:
                    print(path)
        elif cmd == 'clear':
            print('\n' * 150)
        elif cmd == 'mv':
            old_name = cmdargs[0]
            new_name = cmdargs[1]
            if os.path.exists(old_name) and os.path.exists(os.path.join(os.getcwd(), new_name)) == False:
                os.rename(old_name, new_name)
            elif os.path.isfile(old_name) and os.path.isdir(new_name):
                shutil.move(old_name, new_name)
            else:
                print("Error: wrong input")
        elif cmd == 'cp':
            old_name = cmdargs[0]
            new_name = cmdargs[1]
            if os.path.isfile(old_name) and os.path.isdir(new_name):
                shutil.copy(old_name, new_name)
            else:
                print("Error: wrong input")
        elif cmd == 'rm':
            item = ''.join(cmdargs)
            if FSItem(item).isfile():
                os.remove(item)
            elif FSItem(item).isdirectory():
                shutil.rmtree(item)
        elif cmd == 'exit':
            print("Bye bye!")
            break
        else:
            print('Unknown command: {cmd}'.format(cmd=cmd))


if __name__ == '__main__':
    main(sys.argv)