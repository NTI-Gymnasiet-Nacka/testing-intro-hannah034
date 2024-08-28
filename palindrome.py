# Palindrome

def main():
    forward = []
    word = input()
    for i in word:
        forward.append(i)
    backward = forward[::-1]
    if forward == backward:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()
