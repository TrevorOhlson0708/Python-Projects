def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "RavenClaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ").strip().title()
    house = input("House: " ).strip().title()
    return [name, house]

if __name__ == "__main__":
    main()