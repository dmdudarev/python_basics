my_list = ("зима", "зима", "весна", "весна",
           "весна", "лето", "лето", "лето",
           "осень", "осень", "осень", "зима")
my_dict = {1: "зима", 2: "зима", 3: "весна", 4: "весна",
           5: "весна", 6: "лето", 7: "лето", 8: "лето",
           9: "осень", 10: "осень", 11: "осень", 12: "зима"}

my_enter = int(input ("Введите номер месяца: "))
while my_enter < 1 or my_enter > 12:
    my_enter = int(input("Месяц не может быть меньше 1 или больше 12! \nВведите корректный номер месяца: "))
print("*" * 40 +" решение через 'list' "+ "*" * 40)
print (f"{my_enter} месяц - это {my_list[my_enter-1]}")
print("*" * 40 +" решение через 'dict' "+ "*" * 40)
print (f"{my_enter} месяц - это {my_dict.get(my_enter)}")
print("*" * 102)
