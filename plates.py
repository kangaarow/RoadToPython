
def is_valid(s):
    if not (2<= len(s) <= 6):
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    if not s.isalnum():
        return False
    num = False
    for char in s:
        if char.isdigit():
            if not num:
                if char =='0':
                    return False
                num = True
        else :
            if num:
                return False
    return True

def main():
    plate = input("plate: ")
    if is_valid(plate):
        print("valid")
    else:
        print("invalid")

if __name__ == "__main__":
    main()
