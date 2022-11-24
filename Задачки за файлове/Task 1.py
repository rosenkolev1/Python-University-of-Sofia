import os

def better_writelines(file, lines): 
    file.writelines(map(lambda line: "\n" + line, lines))

with open(os.path.join('', 'lorem_ipsum.txt'), 'a+') as fd:
    better_writelines(fd, ["New Line 1", "New Line 2", "New Line 3"])
    #fd.writelines(["New Line 1", "New Line 2", "New Line 3"])
    fd.seek(0)
    content = fd.read()

    print(f'content={content}')





