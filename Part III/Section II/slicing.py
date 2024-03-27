# Slicing

s = slice(0,10,2)

sentence:str = "Lorazepam is a benzodiazepine medication developed by DJ Richards"

tablet_name = slice(0,9)           #makes more readable
print(sentence[tablet_name])


# Easily convert a slice to a range
print(tablet_name.indices(9))