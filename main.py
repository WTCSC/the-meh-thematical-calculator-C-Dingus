import re
        
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
                #add error handeling here
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
            #final.pop()
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
                #add error handeling here
                final.pop()
                final.append(str(float(hold[key_num-1]) * float(hold[key_num+1])))
                skip = True
                read = True
            elif hold[key_num] == "/" and not read:
                #add error handeling here
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
            #final.pop()
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
                #add error handeling here
                final.pop()
                final.append(str(float(hold[key_num-1]) + float(hold[key_num+1])))
                skip = True
                read = True
            elif hold[key_num] == "-" and not read:
                #add error handeling here
                final.pop()
                final.append(str(float(hold[key_num-1]) - float(hold[key_num+1])))
                skip = True
                read = True
            else:
                if skip:
                    skip = False
                else:
                    final.append(hold[key_num])
        if not read:
            #final.pop()
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



i = input(">>")

q = read(i)
print(q)