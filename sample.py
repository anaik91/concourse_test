#/usr/local/bin/python
import time
import sys
import os

def banner(comment):
    size = int(os.popen('tput cols').read().strip())
    print('\n')
    print('#' * size)
    print(comment.center(size))
    print('#' * size)
    
def main():
    print('\n')
    print('************************** Start Job **************************\n')
    print('Time is : {}'.format(time.time()))
    print('Python Version is : {}\n'.format(sys.version))
    print('**************************  End Job   *************************')
    banner('TESTING')
    try:
        os.mkdir('out')
    except FileExistsError as e:
        print('Folder out exists\n')
    with open('out/time','w') as fl:
        fl.write('Time is : {}\n'.format(time.time()))

if __name__ == '__main__':
    main()
