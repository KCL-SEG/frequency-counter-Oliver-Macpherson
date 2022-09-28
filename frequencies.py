"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    count = len(items)
    for i in range(count):
        if str(items[i]) in frequencies.keys(): #or str(items[i]) in frequencies.keys():
            frequencies.update({str(items[i]):frequencies.get(str(items[i]))+1})
        else:
            #frequencies.add({items[i]:1})
            frequencies[str(items[i])] = 1

    return frequencies



#print(frequencies((100, 'Hello', '100', '100', 100)))
