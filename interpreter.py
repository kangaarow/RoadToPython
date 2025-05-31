def main():
    exp = input("enter the expression as x(int) y(op) z(int):")
    x,y,z = exp.split()
    x=int(x)
    z=int(z)

    match y:
        case '*':
            print(f"{x*z: .1f}")
        case '+':
            print(f"{x+z: .1f}")
        case '-':
            print(f"{x-z: .1f}")
        case '/':
            if(z==0):
                print("z cant be zero if y is /")
            else:
                print(f"{x/z: .1f}")
        case _:
            print("invalid operator")

main()
