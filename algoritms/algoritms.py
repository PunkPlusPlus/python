# O(n)
def lineal_search(data, key):
    for i in range(len(data)):
        if key == data[i]:
            return i
    return -1


# O(n^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# O(n log(n))
# O(n^2)
def quick_sort(arr):
    """
    Функция для сортировки массива методом быстрой сортировки.
    """
    if len(arr) <= 1:
        return arr  # Если массив содержит 0 или 1 элемент, он уже отсортирован

    pivot = arr[len(arr) // 2]  # Выбираем опорный элемент (в данном случае, средний элемент)
    left = [x for x in arr if x <= pivot]  # Создаем список элементов меньше опорного

    right = [x for x in arr if x > pivot]  # Создаем список элементов больше опорного

    # Рекурсивно сортируем списки элементов меньших и больших опорного
    return quick_sort(left) + pivot + quick_sort(right)


def generate_bad_character_table(pattern):
    table = {}
    for i in range(len(pattern) - 1):
        table[pattern[i]] = len(pattern) - 1 - i
    return table


# O(n/m)
# O(nm)
def boyer_moore(text, pattern):
    text_len = len(text) # Длина текста
    pattern_len = len(pattern) # Длина паттерна
    if pattern_len == 0:
        return 0  # Пустой паттерн всегда находится в начале строки

    # Генерируем таблицу смещений
    bad_character = generate_bad_character_table(pattern)

    text_index = pattern_len - 1  # Начинаем поиск с последнего символа паттерна
    while text_index < text_len:
        pattern_index = pattern_len - 1  # Итератор для символов паттерна
        # Пока символы паттерна и текста совпадают, сдвигаемся к началу паттерна
        while pattern_index >= 0 and text[text_index] == pattern[pattern_index]:
            text_index -= 1
            pattern_index -= 1
        if pattern_index == -1:   # Если весь паттерн совпал, возвращаем индекс начала вхождения
            return text_index + 1  # Найдено вхождение

        # Используем таблицу смещений для определения сдвига паттерна
        bad_char_shift = bad_character.get(text[text_index], pattern_len)
        # Сдвигаем паттерн на максимально возможное расстояние
        text_index += max(bad_char_shift, pattern_len - pattern_index)

    return -1  # Не найдено

# Пример использования
# text = "cadabra"
# pattern = "abra"
# print("Индекс первого вхождения:", boyer_moore(text, pattern))


# O(log n)
def binary_search(arr, target):
    """
    Функция для выполнения бинарного поиска элемента target в отсортированном списке arr.
    """
    left = 0  # Индекс первого элемента списка
    right = len(arr) - 1  # Индекс последнего элемента списка

    while left <= right:
        mid = (left + right) // 2  # Находим средний индекс
        mid_value = arr[mid]  # Получаем значение элемента по среднему индексу

        if mid_value == target:
            return mid  # Если значение найдено, возвращаем его индекс
        elif mid_value < target:
            left = mid + 1  # Если значение в середине меньше целевого, сужаем интервал поиска вправо
        else:
            right = mid - 1  # Если значение в середине больше целевого, сужаем интервал поиска влево

    return -1  # Если элемент не найден, возвращаем -1

# Пример использования
# arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
# target = 9
# index = binary_search(arr, target)
# if index != -1:
#     print("Элемент {} найден по индексу {}".format(target, index))
# else:
#     print("Элемент {} не найден".format(target))

