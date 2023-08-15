"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа 
X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает 
две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
"""
summ = int(input('Введите сумму загаданных вами двух чисел: '))
mult = int(input('Введите произведение загаданных вами двух чисел: '))
a = 1
b = summ-1
while a+b != sum and a*b != mult:
    if a <= b:
        a+=1
        b-=1
else:
    print(f'Вы загадали числа {a} и {b}')