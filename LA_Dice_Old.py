import random

results_raw = []
results_printer = []
results_list = []
x = int(input("How many dice do you wish to roll?"))
print (x)
for i in range(0,x):
    results_raw.append(random.randint(1,6))
results_printer = results_raw
results_printer.sort()
for i in results_printer:
    if results_printer.count(i) > 1:
        results_printer.append(i + 1)
        for k in range(0,0):
            if j in results_printer == i:
                results_printer.remove(j)
        results_list.append(results_printer)
    else:
        return results_list
        print(results_list)
