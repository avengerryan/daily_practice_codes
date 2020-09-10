
# python locals() : the locals() method updates and returns a dictionary of the
# current local symbol table


"""
raw = locals()
print(locals())
# print(raw)

"""




"""

# example 2: how locals() works inside a local scope

def localsNotPresent():
    return locals()

def localsPresent():
    present = True
    return locals()

print('localsNotPresent:', localsNotPresent())
print('localsPresent:', localsPresent())

"""






# example 3: updating locals( dictionary values

def localsPresent():
    present = True
    print(present)
    locals()['present'] = False
    print(present)

localsPresent()















