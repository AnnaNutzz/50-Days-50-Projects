"""
A simple CLI journal application to input journal date, mood and thoughts
    no reading
"""


while True:
    start =  input("Do you want to start the journal? (y/n): ").strip()

    match start:
        case 'y':

            date = input("\n 📆 Enter today's date: \n")
            mood = input("\n ☀️ On a scale of 1-10 how was your day?: \n")
            thoughts = input("\n ✏️ What happened today?: \n")

            file_path = f"\\path\\{date}.txt"

            with open(file_path, 'w') as file:
                file.write(f"Date: {date} \n\n")
                file.write(f"Today's mood: {mood} \n")
                file.write(f"Today's thoughts: {thoughts}")

        case 'n':
            break

        case _:
            print("INVALID! Try again!")

