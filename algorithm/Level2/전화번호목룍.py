

from tkinter.tix import Tree
from typing import Tuple
from xxlimited import new


def sol(phone_book):
    answer = True
    new_book = list(phone_book)

    for orig in phone_book:
        for new in new_book:
            if orig == new:
                new_book.remove(new)
            elif orig == new[:len(orig)]:
                return False
            else:
                new_book.remove(new)

    return answer

if __name__ == "__main__":
    phone_book = ["119", "97674223", "1195524421"]
    print(sol(phone_book))