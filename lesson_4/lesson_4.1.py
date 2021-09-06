from sys import argv

script_name, hour, rate, bonus = argv

result = float(hour) * float(rate) + float(bonus)

print(result)
