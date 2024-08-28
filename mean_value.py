# Medelvärde

def main():
    numbers = input()
    numbers = numbers.split(', ')
    mean_value = 0
    for i in numbers:
        mean_value += int(i)
    mean_value /= len(numbers)
    print(mean_value)
    
if __name__ == "__main__":
    main()
