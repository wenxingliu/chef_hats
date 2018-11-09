import os
path = r"E:\BaiduNetdiskDownload\215-500\\"

file = os.listdir(path)
#这里复制不能用等号直接赋值 类似指针
filepath = file[:]

for n in range(len(filepath)):
	filepath[n] = path + filepath[n]

for i in range(len(file)):
	oldname_path = filepath[i]
	newname_path = path + str(215+i)+'.png'
	os.rename(oldname_path,newname_path)

print('done!')