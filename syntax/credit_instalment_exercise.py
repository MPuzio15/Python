amount = int(input(
    "This program will calculate your credit instalment. \n Credit amount:\n"))
print(f"Amount: {amount} PLN")
time = int(input("For how long would you like to take credit? \n Years: "))
print(f"Years: {time} ")
interest = float(input("Interest: "))
print(f"Interest: {interest} %")
# dlug = kwota * (1+p/100) **czasu
instalment = amount * (1 + interest / 100) ** time
print("Instalment: ", instalment)
annual_instalments = []
annual_instalment = 0
for i in range(time):
    annual_instalment = amount * interest / 100
amount += annual_instalment
annual_instalments.append(amount)
print("Annual instaments: ", annual_instalments)
