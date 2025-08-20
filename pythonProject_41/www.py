def create_palindrome(s):
    # Приведение строки к нижнему регистру
    s_lower = s.lower()
    # Проверка, является ли строка палиндромом
    if s_lower == s_lower[::-1]:
        return s_lower
    else:
        # Создание нового палиндрома
        reverse_str = s_lower[::-1]
        return f"{s_lower}_i_{reverse_str}"


print(create_palindrome("радар"))  # радар
print(create_palindrome("Радар"))  # радар
print(create_palindrome("тест"))   # тест_iтсет
print(create_palindrome("Python")) # python_inohtyp
print('good')