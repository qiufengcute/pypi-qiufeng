import random
import time
from pynput import keyboard
import os
from pyfiglet import Figlet
import re

v = '1.1.1'

greetings_new_year = [
    '愿你在新的一年里，学习进步，成绩优异！',
    '新年快乐！愿你在新的一年里，变得更有趣，获得更多的关注！',
    '新的一年，新的开始，愿你拥有无限的能量和活力！',
    '新年新气象，愿你心想事成，万事如意，让大家都嫉妒得要命！',
    '愿你在新的一年里，与同学们相处融洽，老师指导有方！',
    '愿你在新的一年里，成为学校里最帅/美的学生！',
    '新年新开始，愿你的梦想在新的一年里都能实现！',
    '愿你在新的一年里，健康快乐，获得更多的成就！'
]

def qiufeng(font="larry3d"):
    f = Figlet(font=font)
    print(f.renderText('QIUFENG'))

def hello_world(font="larry3d"):
    f = Figlet(font=font)
    print(f.renderText('HELLO WORLD'))

def text_3d(text='text',font="larry3d"):
    f = Figlet(font=font)
    print(f.renderText(text))

def version():
    print('版本号:',v,sep='')

def new_year():
    def greeting(num=1):
        if num > 1:
            greet_pass = []
            for i in range(num):
                while True:
                    greet = random.choice(greetings_new_year)
                    if greet not in greet_pass:
                        break
                greet_pass.append(greet)
                print(greet)
                time.sleep(0.8)
        else:
            greet = random.choice(greetings_new_year)
            print(greet)
    n = random.randint(1,5)
    if(n==1):
        print('恭喜你抽中连续祝福，按回车查看')
        input()
        greeting(6)
    else:
        greeting()
    return n

def happy_birthday(name='Player'):
    for i in range(2):
        print('祝你生日快乐~')
        time.sleep(0.8)
    for i in range(2):
        print('祝你生~日快乐~')
        time.sleep(0.8)
    print('祝你生日快乐!')
    time.sleep(0.8)
    print('让我们祝',name,'生日快乐!',sep='')
    time.sleep(0.8)
    print('耶!')

def fib(A,B,nun):
    fib_list = []
    fib_list.append(A)
    fib_list.append(B)
    n = nun - 2
    for i in range(n):
        new = fib_list[i] + fib_list[i+1]
        fib_list.append(new)
    return fib_list

def maze_game(data=None):
    maze_data = None
    def pr_data(pr_data):
        os.system('cls')
        for i in range(len(pr_data)):
            for j in range(len(pr_data[i])):
                print(pr_data[i][j],end='')
            print()

    def start(data=data):
        if data is not None:
            maze_data = data

        else:
            maze_data = [['#','#','#','#','#','#'],
                        ['#','I',' ',' ',' ','#'],
                        ['#',' ',' ','#',' ','#'],
                        ['#','#','#',' ',' ','#'],
                        ['#',' ',' ',' ',' ','#'],
                        ['#','#','@','#','#','#']]
        return maze_data

    maze_data = start()
    pr_data(maze_data)

    def maze_run(x1,y1,x2,y2,maze_data=maze_data):
        win = False
        if maze_data[y2][x2] == '@':
            win = True
        if maze_data[y2][x2] == ' ' or maze_data[y2][x2] == '@':
            maze_data[y2][x2] = 'I'
            maze_data[y1][x1] = ' '
            pr_data(maze_data)
        if win:
            print('恭喜你，通关了！')
            quit()

    def quit():
        exit()

    def on_press(key,maze_data=maze_data):
        for i in range(len(maze_data)):
            if 'I' in maze_data[i]:
                break
        I_y = i
        I_x = maze_data[i].index('I')
        try:
            if key.char == 'w':
                maze_run(I_x,I_y,I_x,I_y-1)
            if key.char == 'a': 
                maze_run(I_x,I_y,I_x-1,I_y)
            if key.char == 's':
                maze_run(I_x,I_y,I_x,I_y+1)
            if key.char == 'd':
                maze_run(I_x,I_y,I_x+1,I_y)
        except AttributeError:
            if key == keyboard.Key.esc:
                quit()

    # 在监听器中注册上面的事件处理函数
    with keyboard.Listener(
        on_press=on_press) as listener:
        listener.join()

def bmi(kg,m):
    bmi = kg / (m * m)
    bmi = str(bmi)
    match = re.search(r'\.\d{2,}', str(bmi))
    if bool(match):
        index = bmi.index('.')
        cc = index + 3
        oe = int(bmi[cc - 1])
        bmi = float(bmi)
        if oe < 5:
            bmi = int(bmi * 10) / 10
        else:
            bmi = int(bmi * 10) / 10
            bmi += 0.1
    return bmi
