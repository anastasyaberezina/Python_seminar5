# Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Что то не работает

from random import randint as k

candies = 2021
gueue_play = 0 # Сколько возьмется за ход
queue1 = 0 # Сколько конфет возьмут игроки
queue2 = 0

def start():
    print('Начинаем игру! ')
    who()

def who():
    rund_number = k(1, 2)
    if rund_number==1:
        player1()
    else:
        player2()


def player1():
    queue_play=int(input(f'На столе осталось {candies} конфет. Игрок 1, сейчас ваш ход: '))
    while gueue_play>28 or gueue_play<0:
        print('Возьмите от 1 до 28 конфет! ')
    candies-=queue_play
    queue1+=queue_play
    if candies>0:
        player2()
    else:
        print('Победил Игрок 1!')    

def player2():          
    queue_play=int(input(f'На столе осталось {candies} конфет. Игрок 2, сейчас ваш ход: '))
    while gueue_play>28 or gueue_play<0:
        print('Возьмите от 1 до 28 конфет! ')
    candies-=queue_play
    queue2+=queue_play
    if candies>0:
        player1()
    else:
        print('Победил Игрок 2!')    
    

    





