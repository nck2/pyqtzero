import os

def chanage_note_to_md(file,categories='Etc',teaser='3'):
    '''file: 확장자만 포함한 file 이름, jekyll의 머릿말을 작성하는 코드'''

    newfile = os.path.splitext(file)[0] + "_1" + os.path.splitext(file)[-1] # 파일이름에 _1 추가함
    # filepath = os.path.join(os.path.abspath('.') ,newfile )                              # 새로운 파일 이름을 포함한 경로 반환
    filepath = os.path.join("c:/Users/SSHS/Desktop/mytest" ,newfile )                              # 새로운 파일 이름을 포함한 경로 반환

    print('filepath',filepath)

    with open(filepath,"w",encoding='utf-8') as g:
#     g.write("---")
        g.write("""---
title: {}
categories: {}
tag: Etc
slug: {}
header:
  teaser: /assets/images/{}.png
---
    """ .format(os.path.splitext(file)[0],categories,os.path.splitext(file)[0],teaser))
        with open(file,'r',encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                g.write(line)

def ipynb_to_md():
    """.ipynb를 템플릿을 이용한 md로 변환"""
    for (path, dir, files) in os.walk("c:/Users/SSHS/Desktop/ex"):
        print(path,dir,files)

    for filename in files:
        ext = os.path.splitext(filename)[-1]
    #     print(ext)
        if ext == '.ipynb':
    #         ext_filename = os.path.join(path,filename)
            ext_filename = path+ "/"+filename

            print(ext_filename)
            os.system(r'jupyter nbconvert --to markdown --template C:/Users/SSHS/Desktop/ex/mytemplate.tpl '+'"' +ext_filename+'"')
            print('*'*10)


    for filename in files:
        ext = os.path.splitext(filename)[-1]
    #     print(ext)
        if ext == '.ipynb':
    #         ext_filename = os.path.join(path,filename)
            ext_filename = path+ "/"+filename
            os.remove(ext_filename)
            print('*'*10)


def filename_change():
    for (path, dir, files) in os.walk("c:/Users/SSHS/Desktop/ex"):

        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.md':
                ext_filename = path+ "/"+filename
                editname = 'c:/Users/SSHS/Desktop/mytest/2018-06-21-' + filename
                print(editname)
                os.renames(ext_filename,editname)
                print("$"*10)
                chanage_note_to_md(editname)

if __name__ == "__main__":
    pass
