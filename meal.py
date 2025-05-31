def main():
    time = input("enter the time:")
    newTime = convert(time)
    if 7<= newTime <=8 :
        print("BreakFast Time")
    elif 12<= newTime <=13 :
        print("Lunch Time")
    elif 18<= newTime <=19 :
        print("Dinner Time")
    else :
        print("")





def convert(time):
    x,y= time.split(":")
    x = float(x)
    y= float(y) / 60
    return (x+y)

if __name__ == "__main__":
    main()
