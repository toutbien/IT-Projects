from cv2 import pointPolygonTest


def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0
 
 # Iterate through the list
	for n in elements:
		# Does this element belong in the resulting list?
		if i % 2 == 0:
			# Add this element to the resulting list
			new_list.append(n)
		# Increment i
		i += 1

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

#list comprehension
languages = ["French", "Russian", "Italian", "English", "Creole", "Spanish" ]
lengths = [len(language) for language in languages]
print(lengths)

#find all the numbers divisible by 3 and 0
zed = [x for x in range (1,103) if x % 3 == 0]
print(zed)

def odd_numbers(n):
        return [x for x in range(0, n+1) if x % 2 !=0 ]
    
print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []