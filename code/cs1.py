def fibonacci(num):
    previous = 0
    current = 1
    for _ in range(num):
        new_fib = previous + current
        print(new_fib)
        previous = current
        current = new_fib

        if __name__ == "__main__":
            num = sys.argv[:]
            print(num)
            fibonacci(int (num[0]))
