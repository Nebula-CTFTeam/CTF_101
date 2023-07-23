import os

file_path = "<path_to_challenge_file>/"
files = os.listdir(file_path)
for i in range(97,123):
    for j in range(97,123):
        try: 
            if i==97 and j==97:
                flag = open(file_path + files[files.index('flag_aa')], 'rb').read()
            else:
                flag += open(file_path + files[files.index('flag_{}{}'.format(chr(i),chr(j)))],'rb').read()
        except:
            continue
flag_pic = open('<path_to_flag_file>/flag.png','wb')
flag_pic.write(flag)