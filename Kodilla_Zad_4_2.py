"""
Zadanie: palindromy
Pamiętaj, że wszystkie zadania, które wysyłasz Mentorowi powinny być umieszczone w Twoim zdalnym repozytorium, jako osobne projekty. W czasie pracy zapisuj więc kolejne commity i prześlij całość na serwer w serwisie GitHub.

Twoim zadaniem będzie napisanie funkcji, która sprawdza, czy dany wyraz jest palindromem. Palindrom to słowo, które czytane od lewej do prawej i od prawej do lewej brzmi tak samo. Przykłady to “kajak” i “potop”.

Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) i zwraca wartość boolean: True/False, mówiącą czy podany tekst jest palindromem.

Podpowiedź
Pamiętaj, że string/tekst, to kolekcja znaków. Znasz już funkcje kolekcji, które pozwalają odnosić się do elementów indeksowanych od początku i od końca.

Do zadania dodaj krótką dokumentację i umieść je w zdalnym repozytorium. Link prześlij Mentorowi.
"""

def palindrome(word):
    """
    Taki sobie "Help" :P 
    Owa "krótka dokumentacja" jeśli dobrze zrozumiałem.
    """
    palindrom = word[::-1]
    ret = False
    if word == palindrom:
        ret = True
    else:
        ret = False
    return ret

print("Palindrom ('potop') - będzie prawda: %s" % palindrome("potop"))
print("Palindrom ('Piotr') - będzie fałsz: %s" % palindrome("Piotr"))

help(palindrome)