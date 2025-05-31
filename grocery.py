def main():
    grocery_item ={}

    try:
        while True:
            item = input("").upper().strip()
            if input:
               grocery_item[item] = grocery_item.get(item,0) + 1
    except EOFError:
        pass
    for item in sorted(grocery_item):
        print(f"{grocery_item[item]} {item}")

if __name__ == "__main__" :
    main()


