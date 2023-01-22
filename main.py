#conding=utf8  
import os
import chardet


def findfile(filepath,suffix):
   '''
   本函数适用于各种文件递归，遍历后的文件path，数据类型为列表list
   最后得到的list为filepath_list
   食用方法
           ·在filepath里填入想遍历的文件夹目录
           ·在suffix里填入文件后缀即可
           ·不要让函数返回值

   '''
   g = os.walk(filepath)  
   for path,dir_list,file_list in g:  
        for file_name in file_list:
            if file_name[-3:] == suffix:
                filepath_list.append(os.path.join(path, file_name))
            else:
                pass


def change(path):
   '''
   本函数适用于两个文件之间的编码转换
   食用方法
           ·path填要转码文件的路径
           ·函数无返回值
           ·函数默认无任何成功提示
            
   '''   
   with open(path, 'r',encoding='gb18030',errors='ignore') as f:
      text = f.read()

   with open(path, 'w', encoding='utf-8') as f:
      f.write(text)


def to_utf(filepath_list):
   '''
   本函数适用于文件的转码
   食用方法
           ·在filepath里填入想转码的文件
           ·注意filepath的数据类型为列表
           ·函数无返回值
           ·本函数依赖上面的change()函数
   '''
   for i in filepath_list:
      change(i)
      print("编码方式已从改为 utf-8")

   


if __name__ == "__main__":
    filepath_list=[]
    filepath = input("请输入想遍历的文件目录")
    findfile(filepath=filepath,suffix=input("请输入文件的后缀"))
    to_utf(filepath_list=filepath_list)
    

