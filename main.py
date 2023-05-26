from typing import Callable, Any


def say_hello(func: Callable) -> Any:
    def wrapper(*args, **kwargs) -> Any:
        print(f"Запускается функция {func.__name__}.\nОписание задачи: {func.__doc__}\n"
              f"Входящие параметры: {args=}, {kwargs=}")
        result: Any = func(*args, **kwargs)
        print(f"Результат выполнения функции {func.__name__}: {result=}\n")
        return result

    return wrapper


@say_hello
def find_different_elements(ar1: list[int], ar2: list[int]) -> set[int]:
    """
    Даны два списка, нужно вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом.
    Оценить эффективность своего решения

    Сложность O(n+m)
    Пояснение:
        1. Приведение list в set = O(n) + O(m)
        2. Разница между множествами O(n)
        3. n + n + m = 2n + m. Константы игнорируются.
    """
    return set(ar1) - set(ar2)


@say_hello
def remove_zeros_for(ar: list[int]) -> list[int]:
    """
    Дан массив целых чисел. Нужно удалить из него нули. Можно использовать только О(1) дополнительной памяти.

    Сложность худшего случая (все 0) O(n^2)
    Пояснение:
        1. Подсчет всех нулей в списке O(n)
        2. Удаление, как и добавление list, O(n)
    """
    count_zeros: int = ar.count(0)
    for i in range(count_zeros):
        ar.remove(0)
    return ar


@say_hello
def remove_zeros_while(ar: list[int]) -> list[int]:
    """
    Дан массив целых чисел. Нужно удалить из него нули. Можно использовать только О(1) дополнительной памяти.
    Сложность худшего случая (все 0) O(n^2)
    Пояснение:
        1. Удаление, как и добавление list, O(n)
    """
    cur: int = 0
    while cur < len(ar):
        if ar[cur] == 0:
            ar.pop(cur)
        else:
            cur += 1
    return ar


@say_hello
def remove_zeros_list_comprehension(ar: list[int]) -> list[int]:
    """
    Дан массив целых чисел. Нужно удалить из него нули. Можно использовать только О(1) дополнительной памяти.
    !Использовано больше памяти
    Сложность O(n)
    Память O(n)
    """
    return [num for num in ar if num != 0]


def main():
    find_different_elements([1, 2, 3], [3, 4, 5])
    remove_zeros_for([0, 1, 2, 0, 0, 0, 3, 4, 1, 2, 4, 6, -1, 56, 0, 8, 4])
    remove_zeros_while([0, 1, 2, 0, 0, 0, 3, 4, 1, 2, 4, 6, -1, 56, 0, 8, 4])
    remove_zeros_list_comprehension([0, 1, 2, 0, 0, 0, 3, 4, 1, 2, 4, 6, -1, 56, 0, 8, 4])


if __name__ == '__main__':
    main()
