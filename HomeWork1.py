# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input('Введите текст: ')

def ABC(text):

    text = [i for i in text.split() if 'абв' not in i]
    return ' '.join(text)

new_text = ABC(text)    
print(new_text)