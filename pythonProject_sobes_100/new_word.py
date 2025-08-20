from collections import deque


def word_ladder(begin_word, end_word, word_list):
    word_set = set(word_list)  # Для быстрого поиска
    if end_word not in word_set:
        return 0  # Невозможно преобразовать

    queue = deque([(begin_word, 1)])  # (слово, шаги)
    visited = set()
    visited.add(begin_word)

    while queue:
        current_word, steps = queue.popleft()

        if current_word == end_word:
            return steps  # Нашли решение!

        # Генерируем все возможные соседи (с 1 изменённой буквой)
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i + 1:]

                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, steps + 1))

    return 0  # Если очередь опустела, а решение не найдено


# Пример использования:
begin_word = "same"
end_word = "cost"
word_list = ["same", "came", "case", "cast", "lost", "last", "cost"]

print(word_ladder(begin_word, end_word, word_list))  # Вывод: 5