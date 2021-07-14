import shutil
import os
src='E:\\Python\\13-Jul-2021\\source\\src_file1.txt'
dst='E:\\Python\\13-Jul-2021\\destinat\\dst_file1.txt'

#list the files in the directory
source1 = os.listdir('E:\\Python\\13-Jul-2021\\source')
print(source1)

#copying file
shutil.copyfile(src,dst)

#move file from onee folder to another
shutil.move(src=r'E:\\Python\\13-Jul-2021\\source\\src_file2.txt',dst=r'E:\\Python\\13-Jul-2021\\destinat\\dst_file2.txt')

#for removing entire folder
src1='E:\\Python\\13-Jul-2021\\source'
shutil.rmtree(src1)

#for removing a file
os.remove("E:\\Python\\13-Jul-2021\\source\\src_file3.txt")

#for removing an empty folder
src2='E:\\Python\\13-Jul-2021\\source\\sourceempty'
os.removedirs(src2)

#for renaming the file
os.rename("E:\\Python\\13-Jul-2021\\source\\src_4.txt","E:\\Python\\13-Jul-2021\\source\\src_rename.txt")
