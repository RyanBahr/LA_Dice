import random

results = []
results1 = []
x = int(input("What is the size of your dice pool?"))
for i in range(0, x):
    results.append(random.randint(1,6))
for i in results:
    for j in results:
            if i == j and results.count(i) > 1: #This calls the same number twice.Solved
                    print("Your results are currently: %s" % results)
                    combine = input("Do you want to combine %s and %s? (1=Y/0=N)" % (i,j))
                    if combine == 1:
                        results.append(i + 1)
                        results.remove(i)
                        results.remove(j)
                    if combine == 0: #Last problem. I want to
                        print("Okay!")
                        results1.append(j)
                        results.remove(j)
else: results = results + results1
print("Your result is %s" % results) 
