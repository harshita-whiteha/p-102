import os
import shutil

from_dir  = "C:/Users/jaideep m/downloads/d"
to_dir = "d:/document_file"
list_of_file = os.listdir(from_dir)
#print(list_of_file)

for file_name in  list_of_file:
    name , ext = os.path.splitext(file_name)
  #  print(ext)

    if ext == " ":
         continue
    if ext in [".pdf" , ".pps"]:
        path1 = from_dir+"/"+file_name
        path2 = to_dir+"/"+"document_file"
        path3 = to_dir+"/"+"document_file"+"/"+file_name

    if os.path.exists(path2):
        print("path exesis " + file_name) 
        shutil.move(path1 , path3)
    else:
        os.mkdir(path2)
        print("path created " + file_name) 
        shutil.move(path1 , path3)
