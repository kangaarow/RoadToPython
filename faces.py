def main():
    userInput = input("enter the emoticon phrase:");
    userInput=convert(userInput)
    print(userInput)

def convert(str):
    str = str.replace(":)","🙂")
    str = str.replace(":(","🙁")
    return str


main()
