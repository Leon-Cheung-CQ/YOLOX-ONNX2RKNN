import os
# 图片文件夹路径
pic_paths= "./lh_data"
f=open('dataset.txt', 'w')
filenames=os.listdir(pic_paths)
filenames.sort()
for filename in filenames:
    out_path = os.path.join(os.path.basename(pic_paths), filename)
    print(out_path)
    f.write(out_path+'\n')
f.close()
