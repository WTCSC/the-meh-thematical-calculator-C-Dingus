import re
import time


def spell(phrase):
    for char in phrase:
        print(char, end = "", flush = True)
        time.sleep(0.02)
    time.sleep(0.2)


def synt(inp):
    operators = r"[-*+/^()]"
    return [item for item in re.split(f"({operators})", inp) if item != ""]

def capture(keys):
    final = []
    found = False
    caught = "" 
    opens = 0

    for key in keys:
        if opens == 0: 
            if key == "(":
                found = True
                opens += 1
            else:
                final.append(key)
        else:
            if key == "(":
                opens += 1
            if key == ")":
                opens -= 1
           
            if opens > 0:
                caught += key
            else:
                final.append(read(caught))
                caught = ""
    if found:
        return final
    return keys


def exponents(keys):
    hold = keys

    while True:
        final = []
        read = False
        skip = False
        for key_num in range(0, len(hold)):
            if hold[key_num] == "^" and not read:
                final.pop()
                final.append(str(float(hold[key_num-1]) ** float(hold[key_num+1])))
                skip = True
                read = True
            else:
                if skip:
                    skip = False
                else:
                    final.append(hold[key_num])
        if not read:
            return final
        else: 
            hold = final


def mult_div(keys):
    hold = keys

    while True:
        final = []
        read = False
        skip = False
        for key_num in range(0, len(hold)):
            if hold[key_num] == "*" and not read:
                final.pop()
                final.append(str(float(hold[key_num-1]) * float(hold[key_num+1])))
                skip = True
                read = True
            elif hold[key_num] == "/" and not read:
                final.pop()
                final.append(str(float(hold[key_num-1]) / float(hold[key_num+1])))
                skip = True
                read = True
            else:
                if skip:
                    skip = False
                else:
                    final.append(hold[key_num])
        if not read:
            return final
        else: 
            hold = final



def add_sub(keys):
    hold = keys

    while True:
        final = []
        read = False
        skip = False
        for key_num in range(0, len(hold)):
            if hold[key_num] == "+" and not read:
                final.pop()
                final.append(str(float(hold[key_num-1]) + float(hold[key_num+1])))
                skip = True
                read = True
            elif hold[key_num] == "-" and not read:
                if len(final) > 0:
                    final.pop()
                    final.append(str(float(hold[key_num-1]) - float(hold[key_num+1])))
                else:
                    final.append(str(0-float(hold[key_num+1])))
                skip = True
                read = True
            else:
                if skip:
                    skip = False
                else:
                    final.append(hold[key_num])
        if not read:
            return final
        else: 
            hold = final



def read(inp):
    keys = synt(inp.replace(" ", ""))
    keys = capture(keys)
    keys = exponents(keys)
    keys = mult_div(keys)
    keys = add_sub(keys)


    return float(keys[0])


spell("Can't you do this yourself? \nc'mon please I don't want to deal with your stupid math questions (leave yes/no)\n>>")
i = input()
if i.lower() == "y" or i.lower() == "yes":
    spell("thank you")
else:
    while True:
        spell("fine what is your dumb math problem \n>>")
        i = input()
        try:
            q = read(i)
            print(q)
        except Exception as e:
            match e:
                case ZeroDivisionError():
                    spell("well done you divided by zero")
                case ValueError():
                    spell("why did you decide to input a letter?")
                case _:
                    print("what the hell did you do?")

        spell("\nplease leave now\n")
        i = input(">>")
        if i.lower() == "no" or i.lower() == "n":
            spell("#$@&\n")
        else:
            spell("#$@& yes get out of here\n")
            break