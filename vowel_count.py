# Vokalräkning

def main():
    vowel = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']
    count = 0
    word = input()
    for i in word:
        if i in vowel:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
