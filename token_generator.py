"""Генератор случайных токенов.

Использует модуль secrets, который создан для безопасной генерации
паролей и ключей (в отличие от обычного модуля random).
"""

import secrets
import string
from pathlib import Path

# ---------- Наборы символов ----------

LETTERS_DIGITS = string.ascii_letters + string.digits
HEX = "0123456789abcdef"
URL_SAFE = LETTERS_DIGITS + "-_"
SYMBOLS = "!@#$%^&*()-_=+?"
STRONG = LETTERS_DIGITS + SYMBOLS

# Номер пункта -> (название, набор символов, нужны ли символы всех видов)
TYPES = {
    "1": ("Буквы и цифры", LETTERS_DIGITS, False),
    "2": ("Hex (цифры 0-9 и буквы a-f)", HEX, False),
    "3": ("URL-safe (буквы, цифры, - и _)", URL_SAFE, False),
    "4": ("Сложный (буквы, цифры и символы)", STRONG, True),
}

MENU = """
================ ГЕНЕРАТОР ТОКЕНОВ ================
Выбери тип токена:
1 - Буквы и цифры
2 - Hex (цифры 0-9 и буквы a-f)
3 - URL-safe (буквы, цифры, - и _)
4 - Сложный (буквы, цифры и символы)
0 - Выход
"""

SAVE_FILE = "tokens.txt"


# ---------- Функции ----------

def is_strong(token: str) -> bool:
    """Проверяет, что в токене есть строчная, заглавная буква, цифра и символ."""
    return (
        any(c.islower() for c in token)
        and any(c.isupper() for c in token)
        and any(c.isdigit() for c in token)
        and any(c in SYMBOLS for c in token)
    )


def generate_token(length: int, alphabet: str, need_all_kinds: bool = False) -> str:
    """Создаёт один случайный токен заданной длины."""
    while True:
        token = "".join(secrets.choice(alphabet) for _ in range(length))
        if not need_all_kinds or is_strong(token):
            return token


def ask_int(question: str, default: int, low: int, high: int) -> int:
    """Спрашивает число. Enter - значение по умолчанию. Повторяет, пока ввод неверный."""
    while True:
        text = input(f"{question} (от {low} до {high}, Enter - {default}): ").strip()
        if not text:
            return default
        if text.isdigit() and low <= int(text) <= high:
            return int(text)
        print("Нужно целое число в указанных пределах, попробуй ещё раз.")


def save_tokens(tokens: list[str]) -> None:
    """Дописывает токены в файл tokens.txt в текущей папке."""
    path = Path(SAVE_FILE)
    with path.open("a", encoding="utf-8") as file:
        for token in tokens:
            file.write(token + "\n")
    print(f"Сохранено в файл: {path.resolve()}")


def main() -> None:
    try:
        while True:
            print(MENU)
            choice = input("Твой выбор: ").strip()

            if choice == "0":
                print("Пока!")
                break
            if choice not in TYPES:
                print("Не понял. Введи цифру от 0 до 4.")
                continue

            name, alphabet, need_all_kinds = TYPES[choice]
            length = ask_int("Длина токена", 32, 8, 256)
            count = ask_int("Сколько токенов создать", 1, 1, 100)

            tokens = [generate_token(length, alphabet, need_all_kinds) for _ in range(count)]

            print(f"\nТип: {name}, длина: {length}\n")
            for token in tokens:
                print(token)

            if input("\nСохранить в файл tokens.txt? (д/н): ").strip().lower() in ("д", "да", "y", "yes"):
                save_tokens(tokens)
    except (EOFError, KeyboardInterrupt):
        print("\nПока!")


if __name__ == "__main__":
    main()