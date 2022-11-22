if __name__ == "__main__":
    idx = 0
    unlocked = False

    # Where main code starts
    while True:
        get = input()

        if not get.isdecimal():
            # remove every character that is not a decimal (0-9)
            pass

        if not len(get) == 0:
            # makes sure something still remains in the string
            for x in get:
                # handle the input string into individual characters
                if x == "8" and idx == 0 or idx == 3:
                    idx += 1
                elif x == "3" and idx