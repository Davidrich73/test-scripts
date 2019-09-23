-- coding: utf-8 -- 

# below to remove apostrophes from .chat file

if file.endswith('.chat'):
    ...
    cleaned = re.sub('<(.|\n)*?>','',content)
    cleaner = string.translate(cleaned, None, ["‘","’"])
    # python3 has to use:
    # # cleaner = cleaned.translate(str.maketrans({'‘':'','’':''}))

 # newtext = text.replace("’", "'") # not sure if i need to use this line


# below is to remove numbers if they exist within .chat file

 def contains_digit(s):
    isdigit = str.isdigit
    return any(map(isdigit,s))

# below to merge new.chat file with the old file from previous week 

def mergeandsort(file1, file2, output):
    fp1, fp2 = open(file1, 'r'), open(file2, 'r')
    merge_data = fp1.read().strip().split("\n") + fp2.read().strip().split("\n")
    merge_data = sorted(l3, reverse=True)
    fp = open(output, 'w')
    for i in merge_data:
        fp.write(i)

    fp.close()
    return True, output


# todo - change the directories below to show the correct directories of the .chat files

p1 = '/home/vivek/Desktop/f1.txt' 
p2 = '/home/vivek/Desktop/f2.txt'    
p3 = '/home/vivek/Desktop/f12.txt' 

print mergeandsort(p1, p2, p3)
