import os
clear = lambda: os.system('cls')
clear()

def player_name_check(name: str) -> bool:
    return player_name == "placeholder"


def define_pronouns() -> tuple:
    pronouns_input = input("Please enter your preferred pronoun for this playthrough (he, she, they, ze, xe): ")
    if pronouns_input == "she" or "s":
        pronouns = gen_pronouns(0)
    elif pronouns_input == "he" or "h":
        pronouns = gen_pronouns(1)
    elif pronouns_input == "they" or "t":
        pronouns = gen_pronouns(2)
    elif pronouns_input == "ze" or "z":
        pronouns = gen_pronouns(3)
    elif pronouns_input == "xe" or "x":
        pronouns = gen_pronouns(4)
    else:
        pronouns = gen_pronouns(failed_pronoun())
    return pronouns


def failed_pronoun() -> int:
    print("You have not entered an understood pronoun. This will default to they/them.")
    confirmed = input("Continue... ")
    return 2


def gen_pronouns(pron_option: int) -> tuple:
    SHE = ("she", "her", "her", "hers", "herself")
    HE = ("he", "him", "his", "his", "himself")
    THEY = ("they", "them", "their", "theirs", "themself")
    ZE = ("ze", "hir", "hir", "hirs", "hirself")
    XE = ("xe", "xem", "xyr", "xyrs", "xemself")

    if(pron_option == 0):
        return SHE
    if(pron_option == 1):
        return HE
    if(pron_option == 2):
        return THEY
    if(pron_option == 3):
        return ZE
    if(pron_option == 4):
        return XE


def story_body():
    print("Welcome")

    input("(Press Enter...)")

    clear()

    player_name = input("Please input your name: ")

    clear()

    print("Welcome", player_name + "!")

    input("(Press Enter...)")

    clear()

    player_pronouns = define_pronouns()

    print("Your pronouns are " + player_pronouns[0] + "/" + player_pronouns[1] + "/" + player_pronouns[3])

    input("(Press Enter...)")

    clear()


story_body()
