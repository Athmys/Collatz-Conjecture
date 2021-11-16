import matplotlib.pyplot as plt

start = int(input("start num: "))

numbers = [start]
iterations = 0

def line_plot(numbers):
    plt.plot(numbers)
    plt.ylabel('Collatz Conjecture')
    plt.show()

def collatz(start, iterations):
    while start != 1:
        if (start % 2) == 0:
            start = start/2
        else:
            start = 3*start+1
        numbers.append(start)
        iterations += 1

    print(iterations)
    line_plot(numbers)
    
collatz(start, iterations)