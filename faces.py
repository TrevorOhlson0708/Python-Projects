def main():
    str = input("How are you feeling?: ")
    print(convert(str))

def convert(str):
    new = str.replace(":)", "🙂").replace(":(", "🙁")
    return new
main()
