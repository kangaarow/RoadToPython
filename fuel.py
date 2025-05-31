def main():
    while True:
        fraction = input("enter the fraction (X/Y): ")
        try:
            x,y = fraction.split("/")
            x = int(x)
            y= int(y)
            if(x>y):
                continue
            result= round(x/y*100)
        except ValueError:
            print("value error")
        except ZeroDivisionError:
            print("Zero division error")
        else:
            if(result<=1):
                print("E")
            elif(result>=99):
                print("F")
            else:
                print(f"{result}%")
            break

if __name__ == "__main__":

    main()




