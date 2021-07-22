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
