import numpy as np
from scipy import stats
def calculate_statistics(array: np.array) -> dict:
    """
    Вычисляет среднее, медиану, стандартное отклонение, моду и размах для заданного массива.
        Параметры:
        array (np.array): Входной массив.
    Возвращает:
        dict: Возвращает словарь со статистическими показателями.
    """
    mean_val = np.mean(array)
    median_val = np.median(array)
    std_dev_val = np.std(array)
    mode_val = stats.mode(array)[0]  # функция mode из scipy.stats возвращает моду и количество
    range_val = np.ptp(array)  # Размах (максимум - минимум)
    return {
        "mean": mean_val,
        "median": median_val,
        "std_dev": std_dev_val,
        "mode": mode_val,
        "range": range_val
    }
# Создаем массив чисел
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5])
# Вызываем пользовательскую функцию для вычисления статистики
stats_results = calculate_statistics(data)
# Печатаем результаты
print("Статистические результаты:")
for key, value in stats_results.items():
    print(f"{key.capitalize()}: {value}")
    
def filter_greater_than_mean(array):
    """
    Фильтрует элементы массива, которые больше среднего.
        Параметры:
        array (np.array): Входной массив.
      Возвращает:
        np.array: Отфильтрованный массив с элементами, большими чем среднее.
    """
    mean_val = np.mean(array)
    filtered_array = array[array > mean_val]
    return filtered_array
# Создаем массив чисел
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5])
# Вызываем пользовательскую функцию для вычисления статистики
filtered_data = filter_greater_than_mean(data)
print("Отфильтрованные данные (больше среднего):", filtered_data)