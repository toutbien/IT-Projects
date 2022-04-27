#enumerating through a list adding a numbered position based on
#position in the list
from unittest import result


winners = ["Drew", "Jay", "Nick", "Prina", "Carl"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))
    
#you have a list of tuples containing email address and a 
#second list with names and you need to combine them using angled brackets < >
def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name,email))
    return result

print(full_emails([("john@mappers.com", "John Pierce"),
                   ("bobby@mappers.com", "Robert Jones")]))

#enumerate to find every other elemtn
def skip_elements(elements):
	element = [x for i, x in enumerate(elements) if i % 2 == 0]
	return element

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']