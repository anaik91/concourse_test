#/usr/local/bin/python
import time
import sys
import os

def main():
    print('\n')
    print('************************** Start Job **************************\n')
    print('Time is : {}'.format(time.time()))
    print('Python Version is : {}\n'.format(sys.version))
    print('**************************  End Job   *************************')
    try:
        os.mkdir('out')
    except FileExistsError as e:
        print('Folder out exists\n')
    with open('out/time','w') as fl:
        fl.write('Time is : {}\n'.format(time.time()))

if __name__ == '__main__':
    main()