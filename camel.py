def main():
    camelCase= input("enter the name for variable in camelcase:")
    snakeCase=''
    for char in camelCase:
        if char.isupper():
            snakeCase+="_" + char.lower()
        else :
            snakeCase+=char
    print(f"snakecase : {snakeCase}")

if __name__ == "__main__":
    main()
