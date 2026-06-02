def get_positive_int():
    x = int(input("Enter valid integer greater than 0: "))

    if x > 0:
        print("thanks for following directions")
    elif x <= 0:
        print("Follow directions better")
        get_positive_int()

get_positive_int()
