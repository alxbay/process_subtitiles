import os
from datetime import datetime
import shutil

path_in = "src"
path_out = "out"

if not os.path.exists(path_in):
    os.mkdir(path_in)

if not os.path.exists(path_out):
    os.mkdir(path_out)

list_all_words = []
list_old_words = []
list_add_words = []
list_raw_words = []
list_new_words = []

# сначала чистим файлы субтитров и сохраняем
for root, dirs, files in os.walk(path_in):
    for filename in files:
        # print(filename)
        f = open(path_in+"\\"+filename, "r", encoding='latin-1')
        ff = open(path_out+"\\"+filename+".txt", "w", encoding='utf-8')
        sentence = ""
        for x in f:
            xx=x.rstrip()
            if (xx.find("-->") < 0)and(len(xx)>0)and(not xx.isnumeric()):
                sentence += (xx +" ")
                if xx[-1] == '.' or xx[-1] == '?' or xx[-1] == '!':
                    # print(sentence)
                    # ff.write(sentence+" | \n")
                    ff.write(sentence+"\n")
                    sentence = ""
        ff.close()
        f.close()
        print("finished: " +filename)
