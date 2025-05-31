def main():
    answer = input("what is the answer to the great question of life, the universe and everything ").lower().strip()
    if check(answer):
        print("yes")
    else:
        print("No")

def check(ans):
    return ans == "42" or ans == "forty-two" or ans =="forty two"

main()

