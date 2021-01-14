import os

base_note = '''# 2021-Eeyes-Back-End-Traincamp-Train-{}

​																																																	By `y=xsinx`

## index
'''

def gen_note(file_path,title,content_list):
    File = open(file_path, "w",encoding="utf-8")
    File.write(base_note.format(title))
    count = 0
    for content in content_list:
        count += 1
        File.write(f"[{count}、{content} ](#{count}. {content})\n\n")

    count = 0
    for content in content_list:
        count += 1
        File.write(f"## [{count}. {content}](#index)\n\n")



root_path = r'C:\Users\24246\Desktop\2021-Eeyes-Back-End-Traincamp'
dir_name = input('Please Input New dir name:')
new_dir_path = os.path.join(root_path,dir_name)
try:
    os.mkdir(new_dir_path)
    print(f'{new_dir_path} 创建成功!')
except:
    result = input('文件夹已存在,是否继续?(y/n)')
    if result == 'y':
        pass
    else:
        exit()

file_name = dir_name+'.md'
file_path = os.path.join(new_dir_path, file_name)

title = input('Please Input the Num:')
content_list = []
while True:
    content = input('Please Input the Content , Enter will Exit:')
    if content == '':
        break
    else:
        content_list.append(content)

gen_note(file_path,title, content_list)
print(f"{file_path} 生成成功")

