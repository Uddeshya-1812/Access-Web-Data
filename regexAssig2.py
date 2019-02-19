import re
file_name = input()
file = list(open(file_name))
list_elements = [line.rstrip('\n') for line in file]
string = ' '.join(list_elements)
y  = re.findall('[0-9]+',string)
y = map(int,y)
sum_of_numbers_in_provided_data = sum(y)
print(sum_of_numbers_in_provided_data)