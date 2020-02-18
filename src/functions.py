"""
asxjsak
"""
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 10)
    print(keywords)
    for kw in keywords:
        print(kw, ":", keywords[kw])


def parrot(voltage, state='a stiff', action='voom'):
     print("-- This parrot wouldn't", action, end=' ')
     print("if you put", voltage, "volts through it.", end=' ')
     print("E's", state, "!")




# cheeseshop('Test',"AA","BB","CC",Key1="DD",key2="EE")
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

parrot(**d)



