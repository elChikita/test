"""
Функции передается путь к файлу.
Возвращает массив значений.
"""
def create_list(file_path):
    inp = open(file_path)
    arr = inp.readlines()

    return arr


"""
Функции передается масив полученый ранее в create_list() 
и аргумент выбора поиска максимального/минимального элемента ('min','max').
Возвращает максимальный/минимальный элемент массива в зависимости от выбора.
В случае указания неверного аргумента выбора в терминал выводится сообщение об ошибке.
"""
def find_minmax(arr, switcher):
    number = 0
    for item in arr:
        item = int(item)
        if switcher == 'min':
            if number > item:
                number = item
        elif switcher == 'max':
            if number < item:
                number = item
        else:
            print('\033[91m'
                  'BecomeADev2020.find_minmax()\nCheck the second argument.'
                  ' This must be a \'min\' or \'max\''
                  '\033[0m')
            return None

    return number


"""
Функции передается масив полученый ранее в create_list().
Возвращается среднее арифметическое массива.
"""
def find_avg(arr):
    summ = counter = 0
    for item in arr:
        item = int(item)
        summ += item
        counter += 1
    avg = summ / counter

    return avg


"""
Функции передается масив полученый ранее в create_list().
Возвращается медиана масива. 
"""
def find_median(arr):
    arr_copy = arr[:]   # Копирование массива для его сортировки.
    arr_copy.sort(key=int)
    arr_length = len(arr_copy)
    if arr_length % 2 == 0:
        right = arr_copy[(arr_length + 1) // 2]
        left = arr_copy[(arr_length - 1) // 2]
        median = (int(right) + int(left)) / 2
    else:
        median = arr_copy[arr_length // 2]

    return median


"""
Функции передается масив полученый ранее в create_list().
Возвращается последняя наибольшая последовательность чисел, которые увеличиватся.
"""
def find_increase(arr):
    counter = 0
    max_counter = 0
    for i in range(len(arr)):
        if int(arr[i]) > int(arr[i-1]):
            counter += 1
            max_counter = counter if max_counter < counter else max_counter
        else:
            counter = 0

    return max_counter


"""
Функции передается масив полученый ранее в create_list().
Возвращается последняя наибольшая последовательность чисел, которые уменьшаются.
"""
def find_decrease(arr):
    counter = 0
    max_counter = 0
    for i in range(len(arr)):
        if i != 0 and i != int(len(arr)):   # Если убрать, то сравнивается первый и последний элемент
            if int(arr[i]) < int(arr[i - 1]):
                counter += 1
                max_counter = counter if max_counter < counter else max_counter
            else:
                counter = 0

    return max_counter
