import re
import numpy
import os.path

base_dir = "/home/9824/darknet/test"
result = "result"
count = 1
final_result = result+str(count)
final_dir =  os.path.join(base_dir,final_result)

def updateCount():
    fin = open("/home/9824/darknet/test/result1", 'r')
    code = fin.read()
    fin.close()
    lines = []
    #lines = code.split('\n')
    average = 0

    for i in range(50000):
        j = 4*i + 3
        second_line = code.split('\n')[j]
        second_line_parts = second_line.split(' ')
        second_line_parts = second_line_parts[3]
        second_line = second_line_parts[:8]
        lines.append(float(second_line)*100)
        #print(lines[i])
        if i%100 == 0:
            print("{}번째 도는 중".format(i))
    mean_of_data = numpy.mean(lines)
    var_of_data = numpy.var(lines)
    code_arr = []
    code_arr.append(str(mean_of_data))
    code_arr.append(str(var_of_data))

    #code = '\n'.join(code_arr)
    code = ' '.join(code_arr)

    fout = open("/home/9824/darknet/test/result2", 'w')
    fout.write(code)
    fout.close()

def updateCount_self():
    fin = open(__file__, 'r')
    code = fin.read()
    fin.close()

    second_line = code.split('\n')[1]
    second_line_parts = second_line.split(' ')
    second_line_parts[2] = str(int(second_line_parts[2])+1)

    second_line = ' '.join(second_line_parts)
    lines = code.split('\n')
    lines[1] = second_line
    code = '\n'.join(lines)

    fout = open(__file__, 'w')
    fout.write(code)
    fout.close()

if __name__ == '__main__':
   #print('This script has run {} times'.format(COUNT))
    updateCount()
    #updateCount_self()
    
