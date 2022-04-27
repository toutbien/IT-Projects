#List & Tuples
from numpy import size


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

result = convert_seconds(6000)
type(result)

hours, minutes, seconds = result
print(hours, minutes, seconds)


#filesize
def file_size(file_info):
    n, t, filesize = file_info
    
    return("{:.2f}".format( filesize / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.2

#iterate over lists/tuples
animals = ["lion", "zebra", "monkey", "elephant"]
chars = 0
for animal in animals:
        chars += len(animal)
        
print("The animals are: {}, average length: {}".format(chars, chars/len(animals)))
