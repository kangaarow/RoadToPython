def main():
    cost = 50
    while cost>0:
        print(f"Amount Due: {cost}")
        amount = int(input("Insert Coin:"))
        if amount not in [5,10,25]:
            print(f"Amount Due: {cost}")
            return
        cost= cost-amount

    print(f"change owed: {cost*-1}")

if __name__ == "__main__":
    main()



