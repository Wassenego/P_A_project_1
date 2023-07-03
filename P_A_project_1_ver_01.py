"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Marek Sýkora
email: MarekSykora78@seznam.cz
discord: Wassenego#1875
"""

import task_template

users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
         
user = input("username:") 
password = input("password:")        

oddelovac = "-" * 40

if user.lower() not in users.keys() or users[user.lower()] != password:
    print("unregistered user, terminating the program..")
    quit()
else:
    print(oddelovac, "\nWelcome to the app, ", user.lower(),"\n" \
          "We have 3 texts to be analyzed.\n",oddelovac, sep="") 

selection = input("Enter a number btw. 1 and 3 to select: ")
if selection not in ["1", "2", "3"]:
    print("You selection is incorrect, terminating the program..")
    quit()
else:
    print(oddelovac)

text = task_template.TEXTS[int(selection) - 1]

split_words = text.split()
words = [a.strip(".,;:?!") for a in split_words]

title_count = [title for title in words if title.istitle() == True] 
# print(title_count)

upper_count = [upper for upper in words if upper.isupper() == True and upper not in title_count] 
# print(upper_count)

lower_count = [lower for lower in words if lower.islower() == True] 
# print(lower_count)

number_count = [number for number in words if number.isdigit() == True] 
# print(number_count)

sum = 0
for i in number_count:
    sum += int(i)
# print(sum)

print(f"There are {len(words)} words in the selected text.")
print(f"There are {len(title_count)} titlecase words.")
print(f"There are {len(upper_count)} uppercase words.")
print(f"There are {len(lower_count)} lowercase words.")
print(f"There are {len(number_count)} numeric strings")
print(f"The sum of all the numbers {sum}")

occurances = {}
for word in words:
    if len(word) not in occurances:
        occurances[len(word)] = 1
    else:
        occurances[len(word)] += 1
    
sorted_keys = list(occurances.keys())
sorted_keys.sort()
sorted_occurances = {s: occurances[s] for s in sorted_keys}

max_occurances = max(occurances.values())
# print(max_occurances)

print(oddelovac)
print("LEN|","OCCURANCES".center(max_occurances),"|NR.", sep="")
print(oddelovac)

for i in sorted_occurances:
    print(f"{str(i).rjust(3)}|{('*' * sorted_occurances[i]).ljust(max_occurances)}|{sorted_occurances[i]}")