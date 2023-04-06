import sys

print(sys.getwindowsversion())

print(len(sys.argv))         # sys 기능1: argv로 파라미터 받기 (ipynb에선 pirnt생략 가능)
print(sys.argv)

while True:
    cmd = input('Prompt>')
    if cmd == 'exit':
        sys.exit()          # sys기능2: exit 빠져나오기(터미널이나 cmd창에 exit치면 빠져나옴)
    print(cmd)


#-----<터미널 실행 결과>-------#
# PS D:\Workspace> C:/Users/YONSAI/anaconda3/Scripts/activate
# PS D:\Workspace> conda activate base
# PS D:\Workspace> cd .\02.Python\07.모듈\
# PS D:\Workspace\02.Python\07.모듈> python .\01.sys.py hello world 
# 3
# ['.\\01.sys.py', 'hello', 'world'] 
# PS D:\Workspace\02.Python\07.모듈> 