'''
Napisać program ,,HotFizzBuzz": program dla liczb od 1 do 100 ma wypisać liczbę,
jeśli liczba jest podzielna przez 2 ma napisać ,,Hot", jeśli przez 3 to ,,Fizz"
jeśli przez 5 to ,,Buzz". Jeśli przez 2 i 3 =>HotFizz, 2i 5 => HotBuzz,
2 i 3 i 5 => HotFizzBuzz, 3 i 5 => FizzBuzz.
'''

two = " Hot "
three = " Fiz "
five = " Buzz "
for i in range(1, 101):
    print(i)
    if(i%2 == 0):
        print(two)
        if(i%3 == 0):
            print(three)
            if(i%5 == 0):
                print(five)
    elif (i % 3 == 0):
        print(three)
        if (i % 2 == 0):
            print(two)
            if (i % 5 == 0):
                print(five)
    elif (i % 5 == 0):
        print(five)
        if (i % 2 == 0):
            print(two)
            if (i % 3 == 0):
                print(three)
