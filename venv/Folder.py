# 1 获取要复制的文件名
old_file_name = input("请输入文件名(需要后缀):")
# 2 打开要复制的文件
f_read = open(old_file_name, 'r')
position = old_file_name.rfind(".")
new_file_name = old_file_name[0:position] + "[复件]" + old_file_name[position:]
# 3 创建一个新的文件
f_write = open(new_file_name, 'w')
# # 4 从old文件中，读取数据，写入到new文件中
# f_read.read()
# f_write.write()
while True:
	content = f_read.read()

	if len(content) == 0:
		break

f_write.write()

# 5 关闭两个文件
f_read.close()
f_write.close()

