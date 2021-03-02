#/usr/local/bin/python
import time
import sys
import os

def main():
    print('\n')
    print('************************** Start Job **************************\n')
    print('Time is : {}'.format(time.time()))
    print('Python Version is : {}\n'.format(sys.version))
    print('OPS Demo in Progress ..........')
    print('Value for DEMO_KEY : {}'.format(os.getenv('DEMO_KEY'))
    print('**************************  End Job   *************************')

if __name__ == '__main__':
    main()
