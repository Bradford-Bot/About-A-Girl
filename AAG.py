inventory = []
def garage():
    print("You have up in the thin four walls of a garage that has seen better days. You don't remeber how you got here but you know that you live here.")
    print()
    print("Within this room along with you is a bed, a cluser of boxes, the door, and the garage door. Despite the fact that some of these items belong to you, you don't"
          " feel like you're home.")
    wdyd = input("What do you look at?").lower()
    if wdyd == "bed":
        print("It's a thin bed, more of a cot. The bedsheets are worn and the pillow looks moth chewed.")
        lob = input("You notice a letter on your bed, do you open it? ").lower()
        if lob == "no":
            print()
        if lob == "yes":
            print("It's a handwritten note, the handwriting is horrid.")
            print()
            print(" Hello Ruby! Welcome to town! I will arrive to your new home in the morning to help you get settled in. See you then! "
                                                                                                                                "- Friday")
    if wdyd == "boxes":
        print("None of these belong to you... Well, besides one box labled: RUBY MIRA. When you open it, you're hit with the smell of ducktape and printer paper."
              "Clothes, socks, old pictures of people you can't recall remembering, and an old stuffed animal of a cat missing one of its bead eyes."
              "\033[31m" "Ruby:" "\033[0m" "I don't want to look at this anymore.")