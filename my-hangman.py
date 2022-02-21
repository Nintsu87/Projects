# Nina Laaksonen 01/2022
# I made this tiny project for learning and keeping me busy.
# Feel free to give some feedback!

def add_letter(letter):
    ifollower = 0
    updateword = ""
    for gletter in theword:
        if letter == gletter:
            updateword = updateword + letter
            ifollower += 1
        else:
            updateword = updateword + guessword[ifollower]
            ifollower += 1
    return updateword
            
def checking_letters(word, letter, list):

    index = word.find(letter)
    if letter in list:
        value = None
        newword = guessword

    elif index > -1:
        newword = add_letter(letter)
        value = True
    
    else:
        newword = guessword
        value = False
    return newword, value

def theprint(number):
    theprintdictionary = {0:"       \n       \n       \n       \n       \n       \n       \n ", 1: "       \n       \n       \n       \n       \n       \n       \n-------", 2: "       \n      |\n      |\n      |\n      |\n      |\n     /|\n-------", 3: "   ____\n      |\n      |\n      |\n      |\n      |\n     /|\n-------", 4: "   ____\n  |   |\n      |\n      |\n      |\n      |\n     /|\n-------", 5: "   ____\n  |   |\n  o   |\n      |\n      |\n      |\n     /|\n-------", 6: "   ____\n  |   |\n  o   |\n  |   |\n  |   |\n      |\n     /|\n-------", 7: "   ____\n  |   |\n  o   |\n \|   |\n  |   |\n      |\n     /|\n-------", 8: "   ____\n  |   |\n  o   |\n \|/  |\n  |   |\n      |\n     /|\n-------", 9:"   ____\n  |   |\n  o   |\n \|/  |\n  |   |\n /    |\n     /|\n-------" ,10: "   ____\n  |   |\n  o   |\n \|/  |   < Oh noees, I'm done!\n  |   |\n / \  |\n     /|\n-------"}
    print(theprintdictionary[number])

def add_safekeeping(list, letter):
    list.append(letter)
    added = ", ".join(list)
    return added


def try_letters():
    feedback = "- Aloitetaas. -"
    safekeepinglist = []
    number = 0
    safekeepings = ""
    global guessword
    while number <= 10:
        theprint(number)
        print(f"\nArvaa tämä {len(theword)}-kirjaiminen sana:\n\n{guessword}\n")
        print("Arvatut: " + safekeepings + "\n")
        print(feedback + "\n")

        if number == 10:
            break

        letter = input("Anna kirjain: ")
        
        if len(letter) == 1:
            guessword, value = checking_letters(theword, letter, safekeepinglist)
            if value == False:
                number += 1
                feedback = "- Väärin meni. -"
            elif value == True and guessword == theword:
                gogo = " * Päästiinpäs sinne, hyvä! * "
                calc = len(gogo) * "-"
                print(f"\n {calc}\n|{gogo}|\n {calc}")
                break    
            elif value == True:
                feedback = "- Oikein! -"
            elif value == None:
                feedback = f"- Olet jo kokeillut: {letter} -"
                number += 1
        elif len(letter) > 1 and letter != theword:
            feedback = "- Et saa arvata yhtä useampaa kirjainta kerralla. -"
            number += 1
            

        elif letter == theword:
            guessword = theword
            print("\n ------------------------------\n| * Arvasit oikein, JIPPII!! * |\n ------------------------------")
            break
        safekeepings = add_safekeeping(safekeepinglist, letter)

def take_theword():
    while True:
        print("Valitse tähän sana niin,\nettei kaverisi näe sitä!")    
        word = input("  : ")
        for letter in word:
            if letter.isdigit():
                continue
            else:
                print("\nEipäs laiteta numeroita!\n")
                break
    return word

theword = take_theword()
guessword = "_" * len(theword)               
                
try_letters()
