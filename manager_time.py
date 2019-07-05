import time
 
class manager_time:
    def __enter__(self):
        self.start_time = time.time()
        self.start_сtime = time.ctime()
         
    def __exit__(self, type, value, traceback):
        print (f'Время начала выполнения кода {self.start_time}\n{self.start_сtime}\nВремя выполнения кода: {time.time()-self.start_time} сек.\nВремя окончания выполнения кода: {time.time()}\n{time.ctime()}')

with manager_time() as x:
  expression = str(input('Введите выражение: '))
list_expression = expression.split(' ')
assert list_expression[0] in ['+', '-', '*', '/'], 'Ошибка! Операция не введена.'
assert len(list_expression) == 3, 'Oшибка! Несоответствие числа операций и аргументов.'
try:
  if list_expression[0] == '+':
    print('Результат: ', int(list_expression[1]) + int(list_expression[2]))
  elif list_expression[0] == '-':
    print('Результат: ', int(list_expression[1]) - int(list_expression[2]))
  elif list_expression[0] == '*':
    print('Результат: ', int(list_expression[1]) * int(list_expression[2]))
  elif list_expression[0] == '/':
    try:
      print('Результат: ', int(list_expression[1]) / int(list_expression[2]))
    except ZeroDivisionError:
      print('Ошибка! Делить на ноль нельзя!') 
except ValueError:
  print('Ошибка! Аргументами могут быть только числа.')
  
