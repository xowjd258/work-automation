import re
COUNT = 1

def updateCount():
    fin = open("/home/9824/test/fixed.py", 'r')
    code = fin.read()
    fin.close()

    second_line = code.split('\n')[1]
    second_line_parts = second_line.split(' ')
    second_line_parts[2] = str(int(second_line_parts[2])+1)

    second_line = ' '.join(second_line_parts)
    lines = code.split('\n')
    lines[1] = second_line
    code = '\n'.join(lines)

    fout = open("/home/9824/test/fixed.py", 'w')
    fout.write(code)
    fout.close()

if __name__ == '__main__':
   #print('This script has run {} times'.format(COUNT))
    updateCount()
