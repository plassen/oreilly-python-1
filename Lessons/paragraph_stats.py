#!/usr/local/bin/python3
"""Count the words, lines and characters in a chunk of text."""

gettysburg = """\
Four score and seven years ago our
fathers brought forth on this continent,
a new nation, conceived in Liberty, and
dedicated to the proposition that
all men are created equal.

Now we are engaged in a great civil war,
testing whether that nation, or
any nation so conceived and so dedicated,
can long endure. Wa are met on
a great battle-field of that war. We have
come to dedicate a portion of that
field, as a final resting place for those
who here gave their lives that that
nation might live. It is altogether
fitting and proper that we should do this."""

charct = len(gettysburg)

lines = gettysburg.split("\n")
linect = len(lines)

wordct = 0
for line in lines:
   words = line.split()
   wordct += len(words)

print("The text contains", linect, "lines,", wordct, "words, and", charct, "characters.")