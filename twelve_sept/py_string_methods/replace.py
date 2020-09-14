
# python string replace() : replaces substring inside
# the replace() method returns a copy of the string where all occurrences of a
# substring is replaced with another substring


# str.replace(old, new[, count])






"""

# e.g.1: using replace()

song = "cold, cold heart"

# replacing 'cold' with 'hurt'
print(song.replace('cold', 'hurt'))

song = 'Let it be, let it be, let it be, let it be'

# replacing only two occurrences of 'let'
print(song.replace('let', "don't let", 2))

"""






# e.g. on string replace()

song = 'cold, cold heart'
replaced_song = song.replace('o', 'e')

# the original string is unchanged
print("Original string:", song)

print("Replaced string:", replaced_song)

song = 'let it be, let it be, let it be'

# maximum of 0 substring is replaced returns copy of the original string
print(song.replace('let', 'so', 0))

































