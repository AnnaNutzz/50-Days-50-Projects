"""
A Simple RPG choose your adv game with multiple choices for the player to 
choose from with many different outcomes
"""

# variables 
has_weapon = 0

# ---------------------------------------------------------------
"""
TAKE THE USER'S NAME AND USE IT IN THE GAME
"""
name = input("YOUR NAME TRAVELLER?🧝🏻: ")


# ---------------------------------------------------------------
"""
MAIN
"""
def main():
    """
    This function starts the game by introducing the player and calling the examine_room function
    """

    print(f"WELCOME TO THIS ADVENTURE {name.upper()}!!")
    start()  # Start the exploration



# ACT I 
# ---------------------------------------------------------------

def start():
    print(f"You awaken with a jolt, heart hammering against your ribs. \nA damp chill clings to the air, and the only light comes from a single flickering candle on a rough wooden table beside you. \nYou have no memory of how you arrived in this dusty, cobweb-draped room. \n")
    answer = int(input(f"What do you do? \n\t1. Examine your surroundings? \n\t2. Search for an exit? \n\t3. Call out for help? \n"))

    if answer == 1:
        examine_room()
    elif answer== 2:
        search_exit(has_weapon)
    else:
        call_out()


def examine_room():
    """
    This function presents the room description, checks for a weapon,
    and allows the player to choose what to examine (symbol or note)
    """

    print(f"You cautiously approach the rough wooden table. The flickering candle throws long, distorted shadows that dance across its surface. \nYou reach out a hand, brushing away dust and cobwebs. Here's what you find:")
    print("A Simple Carved Symbol: Etched into the table surface is a symbol you don't recognize. Is it a warning, a clue, or simply decoration?")
    print("A Hidden Note: Tucked beneath a loose table leg, you find a crumpled piece of parchment. Unfolding it carefully, you strain to read the faded ink in the dim light.")

    # Check for a weapon first
    has_weapon = int(input(f"\nDo you feel anything in your pockets that could be used as a weapon? (1 - Yes, 2 - No) \n"))

    a1 = int(input(f"\nWhat do you do? \n\t1. Check out the symbol? \n\t2. Check the note? \n"))
    if a1 == 1:
        check_symbol(has_weapon)
    else:
        check_note(has_weapon)

    return has_weapon, a1


def check_symbol(has_weapon):
    """
    This function handles what happens when the player chooses to check the symbol
    """

    print(f"The symbol carved into the table surface is a swirling pattern of three interlocking lines. It's difficult to discern the exact design in the flickering candlelight, but it resembles something like this ⛓️")
    a12 = int(input(f"What do you do? \n\t1. Keep checking the table \n\t2. Leave the table \n"))

    if a12 == 1:
        # Check the note (recursive call)
        check_note(has_weapon)  # Pass the weapon status to the note function
    else:
        search_exit(has_weapon)
        pass


def check_note(has_weapon):
    """
    This function handles what happens when the player chooses to check the note
    """

    print(f"You check the note kept on the table. The moment you touch it, it flies right into your face \nYou can kind of make out how the note looks like a mouth is being formed. \nSuddenly it screams: \n\t")
    print(f"OH {(name).upper()}! WHAT ARE YOU DOING HERE? WAKE UP! \n WAKE UP!! \n  WAKE UPPPP!!!!!")

    if has_weapon == 1:     # Checks if the player has a weapon
        a13 = int(input(f"You notice you have a weapon! Do you? \n\t1. Save the weapon for a rainy day? \n\t2. Tear the note using the weapon? \n"))

        if a13 == 1:
            didnt_kill_note()   # Pass the weapon status to the didnt kill function
        else:
            print(f"You grab hold of the note, choke the 'mouth' with the weapon and pull the note apart! \n")
            tear_note()
    else:
        didnt_kill_note()


def didnt_kill_note():
    """
    This function handles what happens when the player chooses to not tear the note apart
    """

    print(f"The note grows bigger and bigger and BIGGER! \n\tUntil you whole world was claimed pitch black!")
    print(f"Ending 1 - Died to a note!")      # lost the game


def tear_note():
    """
    This function handles what happens when the player chooses to tear the note
    """

    print(f"The note turns into ashes and from the ashes rises a door! \n")
    winning_note_choice = int(input(f"Do you \n\t1. Open the door? \n\t2. Go back to examining the room?"))

    if winning_note_choice == 1:
        win()       # won the game
    else:
        examine_room()


# ACT II
# ---------------------------------------------------------------
def search_exit(has_weapon):
    """
    This function handles searching for an exit and the consequences based on player choices
    """

    print(f"Panic starts to rise in your chest. You need to get out of here! You scan the dusty room, searching for any sign of an escape.\n")
    exit_direction = int(input(f"You see two potential exits: \n\t1. A narrow passage on the LEFT. \n\t2. A heavy wooden door on the RIGHT. \n Which way do you go? \n"))
    
    # Left Passage - Baby Alligator
    if exit_direction == 1:  
        print(f"You squeeze through the narrow passage, the rough stone scraping against your back. The air grows thick and humid, and a low growl pierces the silence. \nEmerging into a small chamber, you come face-to-face with a menacing...")
        print(f"...baby alligator! Its beady eyes glint in the dim light, and its jaws snap menacingly. \n For a baby it had strong enough jaws to chew a human! \n")

        if has_weapon == 1:
            # Player has a weapon (choice for attack or sneak)
            alligator_choice = int(input(f"\t1. Attack the alligator with the weapon? \n\t2. Try to sneak past the alligator? \n"))
            if alligator_choice == 1:
                # Player attacks (WIN)
                print(f"With a mighty swing, you smash the weapon against the alligator's head. It lets out a screech and thrashes around before going limp. \nTaking a deep breath, you continue down the passage, a newfound confidence filling you after you kill a baby alligator...")
                alli_win()     
                return True  
            else:
                # Player tries to sneak (LOSE)
                print(f"Holding your breath, you inch past the alligator, praying it doesn't notice you. Suddenly, it lunges! \nYou scream as razor-sharp teeth clamp down on your leg. The world fades to black. \n")
                print(f"Ending 2 - Died to a baby alligator!")      # lost the game
                return False  
        else:
            # Player has no weapon (LOSE)
            print(f"You stare at the baby alligator, defenseless. It charges, a blur of teeth and claws. There's nothing you can do. \nThe darkness claims you as the alligator's feeding frenzy begins. \n")
            print(f"Ending 2 - Died to a baby alligator!")      # lost the game
            return False  
    
    # Right Door - Viking Bar   
    elif exit_direction == 2:
        vikings()
        return True


def alli_win():
    """
    This function handles the winning fight between the player and the alligator
    """
    print(f"You notice the alligator in it's last breathes throws up a silver key! \nYou obviously reach for it and continue your passage. \n")
    vikings()
    return True


def vikings():
    """
    This function handles the right door to the viking bar
    """
    print(f"You push open the heavy wooden door with a creak. A cacophony of shouts and laughter assaults your ears. Inside, a boisterous group of vikings are celebrating around a massive table. \nThey turn their attention to you, eyeing you with suspicion.")
    
    viking_choice = int(input(f"\nThey bellow in a rough language. A burly viking with an eyepatch steps forward. \n'Who are you, and what brings you to our mead hall?' \n\t1. You stammer out an explanation of your predicament. (Tell the truth) \n\t2. You try to blend in and act like a viking. (Fake it) \n"))
    
    if viking_choice == 1:
        # Player tells the truth (handled previously)
        print(f"You stammer on your words. \n'I- I am lost and I need help! I d-don't know how but I believe someone trapped me here and I- need to get out of here immediately.', you sob")
        print(f"The vikings look at each confused, then face you and laugh. 'OH! We can help the lil' guy out that is no issue', he turns towards his mates. \n'Come on here have a drink with us first!', the viking said while slipping in you a key... \n\tnow you have 2 keys. \nThe vikings take you to a VERY huge door.")
        key = int(input(f"Which key do you use? \n\t1. the alligator's? \n\t2. the vikings? \n"))

        if key:
            key_real = (f"1. i am sure \n2. let me think again \n")
            
            if key_real == 1:
                print(f"You put the key in the key hole and the hole in and the hole instead of turning turns huge and envolopes your world in utter darkness! \n")
                lose()
                return False
            else:
                print(f"You search around the door finding for clues wondering why do you have 2 keys. \nYou feel another hole way above for you to reach. 'Need a lil' hand mate?', asks the burly viking. \nYou nod and he put you top of his 6'8 frame and you both push in the key together and turn. \n")
                win()
        pass  
    else:
        # Player tries to fake it (LOSE)
        print(f"You puff out your chest and attempt to imitate the guttural laughter of the vikings, raising a clenched fist in the air. 'Glory to Odin!' you bellow. \nThe room falls silent. The eyepatch viking stares at you with a piercing gaze. \n'That greeting is for warriors,' he growls. 'And your accent... it betrays you, outsider.' \nUh oh. The vikings erupt in angry shouts, reaching for their axes. \nYour... \n")
        vik_lose()
        return False 





# ACT III
# ---------------------------------------------------------------

def call_out():
    print(f"The earth under your feet starts to tremble! A huge ORC comes into the room. \n")
    ans = input(f"What do you do? \n\t1. beg for help \n\t2. beg for help??")
    lose()



# ---------------------------------------------------------------
"""
WINNING AND LOSING
"""

def win():
    print(f"YOU NOTICE YOU GOT OUT OF THE MAZE! \n\t   YOU WIN!! 🎉")

def lose():
    print(f"YOU GOT EATEN! \n\t  YOU LOSE! 💀")

def vik_lose():
    print(f"Your whole body is dismembered! \n\t  YOU LOSE! 💀")




if __name__ == "__main__":
    main()
