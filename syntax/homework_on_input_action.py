'''
Napisać program który pyta użytkownika ile razy ma daną cyfrę napisać w termianalu:
gdy użytkownik poda '4' – program napisze: 4444.
'''
print("Provide the n number. It will be returned in the console n times: \n")
number = int(input())
print(str(number) * number)
