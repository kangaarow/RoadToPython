def main():
    cap = input("twitter caption:")
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    output = ''
    for char in cap:
        if char in vowel:
            continue
        else:
            output+= char
    print(f"output: {output} ")


if __name__ == "__main__":
    main()
