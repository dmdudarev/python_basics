profit = int(input("Введите Вашу прибыль (руб.): "))
costs = int(input("Введите Вашы издержки (руб.): "))

if profit < costs:
    print(f"Ваши убытки составили {costs - profit:.2f} руб.")
elif profit == costs:
    print("Ваша рентабельность равна нулю")
else:
    print(f"Ваша рентабельность составила {profit - costs:.2f} руб.")
    staff = int(input("Введите количество Ваших сотрудников: "))
    print(
        f"В среднем каждый сотрудник приносит Вашей организации {profit / staff:.2f} руб. (из них чистой прибыли {(profit - costs) / staff:.2f} руб.)")
