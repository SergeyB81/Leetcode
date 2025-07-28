# Определяем класс Solution, в котором содержатся методы для решения задачи
class Solution:

    # Приватный метод для преобразования слова в числовое представление
    def get_num_repr(self, word):
        # Словарь, отображающий буквы 'a'-'j' в цифры '0'-'9'
        codes = {
            'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4',
            'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9'
        }

        s = ''  # Строка, в которую будет собираться числовое представление
        for l in word:
            s = s + codes[l]  # Последовательно заменяем каждую букву на соответствующую цифру

        return int(s)  # Преобразуем полученную строку в целое число

    # Метод для проверки, равна ли сумма числовых значений двух слов значению третьего
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        # Проверяем: firstWord + secondWord == targetWord (в числовом виде)
        return self.get_num_repr(firstWord) + self.get_num_repr(secondWord) == self.get_num_repr(targetWord)


    # Основной блок запускается, если скрипт выполняется напрямую
if __name__ == ('__main__'):  # <- Здесь ошибка: должно быть if __name__ == '__main__'
    print('sergey')

    # Тестовый набор: [первое слово, второе слово, целевое слово, ожидаемый результат]
    test_cases = [['acb', 'cba', 'cdb', True],['acb', 'cba', 'cdb', True],['acb', 'cba', 'cdb', False]]

    # Пример использования метода для одного слова
    print(Solution().get_num_repr('cda'))  # Должно вывести 230 (c=2, d=3, a=0)

    # Проверка всех тестов
    for test_case in test_cases:
        # Проверяем, соответствует ли результат ожидаемому значению
        assert Solution().isSumEqual(*test_case[:3]) == test_case[3]
        print(f"Тест пройден: {test_case}")
        #rep 04