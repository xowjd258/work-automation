text_file_path = "/home/9824/darknet/test/resnet50.cfg"
new_text_content = ''
target_word = '[convolutional_acc]'
new_word = '[convolutional]'
triger = 0
with open(text_file_path,'r') as f:
    lines = f.readlines()
    for i, l in enumerate(lines):
        if triger == 1 and l.find('[convolutional]') != -1:
            triger = 0
            print('line {},triger is off'.format(i))
            new_string = l.strip().replace(new_word,target_word)

        else:
            if l.find('convolutional_acc') != -1:
                triger = 1
                print('line {} triger is on'.format(i))
            new_string = l.strip().replace(target_word,new_word)

        if new_string:
            new_text_content += new_string + '\n'
        else:
            new_text_content += '\n'



with open(text_file_path,'w') as f:
    f.write(new_text_content)
