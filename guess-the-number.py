from random import randint
list_answ_yes = ['yes', 'y', 'да', 'д']


def rules():
  print('Добро пожаловать в игру угадай число!')
  print('Программа загадывает случайное число в указанном пользователем диапазоне.')
  answer = input('Готовы ли вы испытать свою удачю и начать игру? ').lower()



  if answer in list_answ_yes:
    a = int(input('Укажите начальное число диапазона: '))
    b = int(input('Укажите конечное число диапазона: '))
    # print(answer)
    game(a, b)
  else:
    pass
  




def game(a, b):
  attemts = 1
  num = randint(a, b)
  guess = int(input('Введите свое число: '))

  
  while True:
    if guess > b or guess < a:
      print('Вы ввели число за границами значений. Будьте внимательнее, пожалуйста!')
    else:
      if guess == num:
        print(f'Вы сделали это! Число было: {num}. Вы сделали это за {attemts} попыток')
        break
      else:
        if guess > num:
          print('Почти, попробуйте еще раз, но меньше')
          attemts += 1
          guess = int(input('Введите свое число: '))
        else:
          print('Почти, попробуйте еще раз, но больше')
          attemts += 1
          guess = int(input('Введите свое число: '))

      
      
    



rules()