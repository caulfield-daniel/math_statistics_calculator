from mathstats import Statistics

class Calculator:
   """
   Класс Calculator предоставляет интерфейс для вычисления математических статистических показателей.
   """

   def __init__(self):
       """
       Инициализирует объект Calculator и выводит приветственное сообщение.
       """
       print(
           """
           ############################
           *** MATHSTATS CALCULATOR ***
           ############################
           """
       )

   def get_user_input(self):
       """
       Выводит меню выбора действия и возвращает ввод пользователя.
       """
       print(
           """
           Выберите действие 
           1 - Вычислить мат. ожидание
           2 - Вычислить дисперсию
           3 - Вычислить квадратичное отклонение
           0 - Выход
           """
       )
       return input(">>> ")

   def collect_input_data(self):
       """
       Собирает данные от пользователя в формате 'значение:вероятность' и возвращает словарь с данными.
       """
       input_data = {}
       print(
           """
           Введите значения в формате 'значение:вероятность'. 
           Чтобы закончить ввод значений оставьте строку ввода пустой
           """
       )
       while True:
           user_input = input(">>> ")
           if user_input == "":
               break
           try:
               x, p = map(float, user_input.split(":"))
               input_data[x] = p
           except ValueError:
               print("Неверный формат ввода. Попробуйте еще раз.")
       return input_data

   def calculate_and_display(self, calculation_method):
       """
       Вычисляет и выводит результат вычисления с помощью заданного метода.
       """
       input_data = self.collect_input_data()
       try:
           result = calculation_method(input_data)
           print("Результат: {}".format(result))
       except (TypeError, ValueError) as e:
           print(f"Ошибка: {e}")

   def calculate_expectation(self):
       """
       Вычисляет и выводит математическое ожидание.
       """
       self.calculate_and_display(Statistics.expectation)

   def calculate_dispersion(self):
       """
       Вычисляет и выводит дисперсию.
       """
       self.calculate_and_display(Statistics.dispersion)

   def calculate_standart_deviation(self):
       """
       Вычисляет и выводит квадратичное отклонение.
       """
       self.calculate_and_display(Statistics.standard_deviation)

   def run(self):
       """
       Запускает основной цикл программы, обрабатывает ввод пользователя и вызывает соответствующие методы.
       """
       while True:
           user_input = self.get_user_input()
           if user_input == "1":
               self.calculate_expectation()
           elif user_input == "2":
               self.calculate_dispersion()
           elif user_input == "3":
               self.calculate_standart_deviation()
           elif user_input == "0":
               break
           else:
               print("Неверный выбор. Попробуйте еще раз.")
