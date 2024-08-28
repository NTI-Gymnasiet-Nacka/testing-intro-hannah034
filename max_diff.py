# Största skillnad
def main():
    numbers = input()
    max_value = 0
    numbers = numbers.split(', ')
    for i in numbers:
        for j in numbers:
            value = int(i) - int(j)
            if value > max_value:
                max_value = value
    print(max_value)


if __name__ == "__main__":
    main()
