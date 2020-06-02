#palindrome
word = input("Insert any word. Program will check if that is a palindrome. \nWord: ")
is_palindrome = True

for i in range(len(word)):
    if(word[i].lower() !=word[-i -1].lower()):  #przeszukujemy w odwrotnej kolejnosci, zaczynamy od konca i idziemy o jeden step w t
        czyPalindrom = False
        break
print(f"Is {word} a palindrome? {is_palindrome}")
