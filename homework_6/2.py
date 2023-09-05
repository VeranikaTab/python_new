# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from _1_7 import check
from sys import argv

print(check(argv[1]))
