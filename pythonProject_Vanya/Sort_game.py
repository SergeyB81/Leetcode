"""
ИГРА ДЛЯ ИЗУЧЕНИЯ СОРТИРОВОК
Для детей 9-13 лет
"""

import random
import time


# ========== АЛГОРИТМЫ СОРТИРОВКИ ==========

def bubble_sort(arr):
    """
    ПУЗЫРЬКОВАЯ СОРТИРОВКА (Bubble Sort)

    Как работает: большие числа "всплывают" в конец как пузырьки
    """
    arr = arr.copy()  # чтобы не испортить оригинал
    n = len(arr)
    steps = []  # запоминаем шаги для игры

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Меняем местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append((arr.copy(), f"Меняем {arr[j + 1]} и {arr[j]}"))

    return arr, steps


def selection_sort(arr):
    """
    СОРТИРОВКА ВЫБОРОМ (Selection Sort)

    Как работает: ищем самый маленький элемент и ставим его в начало
    """
    arr = arr.copy()
    n = len(arr)
    steps = []

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            steps.append((arr.copy(), f"Ставим {arr[i]} на место {i + 1}"))

    return arr, steps


def insertion_sort(arr):
    """
    СОРТИРОВКА ВСТАВКАМИ (Insertion Sort)

    Как работает: как раскладывание карт - берем новую и вставляем в нужное место
    """
    arr = arr.copy()
    steps = []

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        steps.append((arr.copy(), f"Вставляем {key} на место {j + 2}"))

    return arr, steps


def quick_sort_step_by_step(arr):
    """
    БЫСТРАЯ СОРТИРОВКА (Quick Sort) с записью шагов

    Как работает: выбираем капитана, все кто меньше - налево, кто больше - направо
    """
    steps = []

    def quick_sort_recursive(arr, depth=0):
        if len(arr) <= 1:
            return arr

        captain = arr[len(arr) // 2]
        left = []
        middle = []
        right = []

        for x in arr:
            if x < captain:
                left.append(x)
            elif x == captain:
                middle.append(x)
            else:
                right.append(x)

        steps.append(
            (left + middle + right, f"Капитан {captain}: {'<' if left else ''} {captain} {'>' if right else ''}"))

        return quick_sort_recursive(left, depth + 1) + middle + quick_sort_recursive(right, depth + 1)

    result = quick_sort_recursive(arr.copy())
    return result, steps


# ========== ИГРОВЫЕ КЛАССЫ ==========

class SortingGame:
    """Игра для изучения сортировок"""

    def __init__(self, player_name="Игрок"):
        self.player_name = player_name
        self.score = 0
        self.level = 1
        self.algorithms = {
            "1": {
                "name": "Пузырьковая",
                "func": bubble_sort,
                "description": "⚡ Пузырьковая - большие числа всплывают как пузырьки",
                "hint": "Смотрим на соседей и меняем, если нужно"
            },
            "2": {
                "name": "Выбором",
                "func": selection_sort,
                "description": "🎯 Выбором - ищем самый маленький и ставим в начало",
                "hint": "Найди самый маленький и поставь его на место"
            },
            "3": {
                "name": "Вставками",
                "func": insertion_sort,
                "description": "🃏 Вставками - как карты в руке, вставляем в нужное место",
                "hint": "Представь, что раскладываешь карты"
            },
            "4": {
                "name": "Быстрая",
                "func": quick_sort_step_by_step,
                "description": "🚀 Быстрая - выбираем капитана и делим отряд",
                "hint": "Кто будет капитаном? Все кто меньше налево, кто больше направо"
            }
        }

    def show_menu(self):
        """Показывает меню игры"""
        print("\n" + "=" * 60)
        print(f"🎮 ПРИВЕТ, {self.player_name}! ТВОИ ОЧКИ: {self.score}")
        print("=" * 60)
        print("\nВыбери алгоритм для изучения:")

        for key, algo in self.algorithms.items():
            print(f"{key}. {algo['description']}")

        print("5. 🏆 Соревнование (все алгоритмы)")
        print("6. 📊 Статистика")
        print("0. Выход")

        return input("\nТвой выбор: ")

    def play_algorithm(self, algo_key):
        """Игра с одним алгоритмом"""
        algo = self.algorithms[algo_key]

        print(f"\n{'-' * 50}")
        print(f" УРОВЕНЬ {self.level}: {algo['name']} сортировка")
        print(f" Подсказка: {algo['hint']}")
        print(f"{'-' * 50}")

        # Создаем случайный массив
        size = min(5 + self.level, 8)  # увеличиваем сложность с уровнем
        numbers = [random.randint(1, 9) for _ in range(size)]
        original = numbers.copy()

        print(f"\nЧисла: {numbers}")

        # Получаем результат и шаги
        sorted_numbers, steps = algo['func'](numbers)

        # Игра - угадай количество шагов
        print(f"\n🔍 Сколько раз числа менялись местами?")

        # Показываем процесс пошагово (для обучения)
        if input("Показать подсказку? (д/н): ").lower() == 'д':
            print("\n📝 Смотри как это работает:")
            for i, (step_arr, desc) in enumerate(steps[:3], 1):  # покажем первые 3 шага
                print(f"  Шаг {i}: {desc} -> {step_arr}")

        # Игрок угадывает
        try:
            answer = int(input("\nТвой ответ: "))
            if answer == len(steps):
                print(f"✅ Правильно! +10 очков")
                self.score += 10
            elif abs(answer - len(steps)) <= 2:
                print(f"👍 Почти! Было {len(steps)} обменов. +5 очков")
                self.score += 5
            else:
                print(f"❌ Не угадал. Было {len(steps)} обменов")

            print(f"Результат: {original} -> {sorted_numbers}")

        except ValueError:
            print("Ой! Нужно ввести число")

        self.level += 1
        input("\nНажми Enter чтобы продолжить...")

    def tournament(self):
        """Соревнование всех алгоритмов"""
        print("\n" + "🏆" * 20)
        print(" ТУРНИР АЛГОРИТМОВ")
        print("🏆" * 20)

        # Создаем одинаковые данные для всех
        numbers = [random.randint(1, 9) for _ in range(6)]
        print(f"\nЧисла: {numbers}")

        results = []

        # Тестируем каждый алгоритм
        for algo in self.algorithms.values():
            print(f"\n⏳ {algo['name']} сортировка...")
            time.sleep(1)  # для интриги

            # Замеряем время
            start = time.time()
            sorted_nums, steps = algo['func'](numbers)
            elapsed = time.time() - start

            results.append({
                'name': algo['name'],
                'steps': len(steps),
                'time': elapsed * 1000,  # в миллисекундах
                'result': sorted_nums
            })

        # Показываем результаты
        print("\n" + "📊 РЕЗУЛЬТАТЫ ТУРНИРА:")
        print("-" * 40)

        # Сортируем по количеству шагов
        results.sort(key=lambda x: x['steps'])

        for i, res in enumerate(results, 1):
            medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, "  ")
            print(f"{medal} {res['name']}: {res['steps']} шагов ({res['time']:.2f} мс)")

        print(f"\nВсе алгоритмы справились!")
        self.score += 20
        input("\nНажми Enter чтобы продолжить...")

    def show_stats(self):
        """Показывает статистику"""
        print("\n" + "📊" * 20)
        print(" ТВОЯ СТАТИСТИКА")
        print("📊" * 20)

        print(f"\nИгрок: {self.player_name}")
        print(f"Уровень: {self.level}")
        print(f"Очки: {self.score}")

        # Советы по улучшению
        print("\n💡 Советы:")
        if self.score < 50:
            print("  • Начни с пузырьковой сортировки - она самая простая")
            print("  • Смотри подсказки, они помогут понять логику")
        elif self.score < 100:
            print("  • Ты молодец! Попробуй быструю сортировку")
            print("  • Обрати внимание на сортировку вставками")
        else:
            print("  🏆 Ты настоящий чемпион по сортировкам!")
            print("  • Можешь объяснить друзьям как это работает")

        input("\nНажми Enter чтобы продолжить...")

    def run(self):
        """Запускает игру"""
        print("\n" + "🎮" * 25)
        print(" ДОБРО ПОЖАЛОВАТЬ В ИГРУ 'СОРТИРУЙ-КА'!")
        print(" Здесь ты научишься сортировать числа как настоящий программист")
        print("🎮" * 25)

        while True:
            choice = self.show_menu()

            if choice == "0":
                print(f"\n👋 Пока, {self.player_name}! Ты набрал {self.score} очков")
                print("Приходи еще играть!")
                break
            elif choice in self.algorithms:
                self.play_algorithm(choice)
            elif choice == "5":
                self.tournament()
            elif choice == "6":
                self.show_stats()
            else:
                print("❌ Неправильный выбор. Попробуй снова!")


# ========== ДОПОЛНИТЕЛЬНЫЕ ИГРЫ ==========

class CardGame:
    """Игра с карточками для визуализации"""

    @staticmethod
    def show_card_sort():
        """Показывает как сортировать карточки"""
        print("\n🃏 ИГРА С КАРТОЧКАМИ")
        print("Возьми настоящие карточки с числами и попробуй:")

        cards = [5, 2, 8, 1, 9]
        print(f"\nТвои карты: {cards}")

        print("\n1. Пузырьковая - меняй соседние карты")
        print("2. Выбором - ищи самую маленькую карту")
        print("3. Вставками - бери карту и вставляй в нужное место")

        # Симуляция
        print("\nСмотри как это работает на компьютере:")
        for i in range(len(cards) - 1):
            if cards[i] > cards[i + 1]:
                cards[i], cards[i + 1] = cards[i + 1], cards[i]
                print(f"  Меняем {cards[i + 1]} и {cards[i]}: {cards}")


class SpeedTest:
    """Тест на скорость"""

    @staticmethod
    def test_your_speed():
        """Проверь как быстро ты сортируешь"""
        print("\n⏱️ ТЕСТ НА СКОРОСТЬ")

        numbers = [3, 1, 4, 1, 5, 9, 2, 6]
        print(f"Запомни числа: {numbers}")
        time.sleep(2)
        print("\nА теперь отсортируй их в уме!")

        start = time.time()
        input("Нажми Enter когда закончишь...")
        elapsed = time.time() - start

        print(f"\nТы справился за {elapsed:.1f} секунд!")
        if elapsed < 5:
            print("🚀 Супер-быстро!")
        elif elapsed < 10:
            print("👍 Хорошо!")
        else:
            print("🐢 Попробуй еще разок")


# ========== ЗАПУСК ИГРЫ ==========

if __name__ == "__main__":
    # Приветствие
    print("=" * 60)
    print(" " * 15 + "СОРТИРУЙ-КА")
    print("=" * 60)

    # Спрашиваем имя
    name = input("\nКак тебя зовут? ").strip()
    if not name:
        name = "Чемпион"

    # Создаем и запускаем игру
    game = SortingGame(name)

    try:
        game.run()
    except KeyboardInterrupt:
        print(f"\n\n👋 До свидания, {name}! Заходи еще!")
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        print("Но не волнуйся, это тоже часть обучения!")

    # Показываем дополнительную игру
    print("\n" + "=" * 60)
    print("Хочешь попробовать игру с настоящими карточками?")
    if input("(д/н): ").lower() == 'д':
        CardGame.show_card_sort()
