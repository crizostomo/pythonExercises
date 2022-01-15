from collections import defaultdict, Counter

my_text = "Hello, good luck in programming in Python my friend"
my_text = my_text.lower()

#shows = {}
shows = defaultdict()


shows = Counter(my_text.split())
print(shows)

for word in my_text.split():
    until_now = shows.get(word, 0)
    shows[word] = until_now + 1
    print(word, until_now)

for x in 'Diogo':
    print(x)

text1 = "Hello, good luck in programming in Python my friend"
print(Counter(text1))

shows1 = Counter(text1.lower())
total_characters = sum(shows1.values())
for letter, frequency in shows1.items():
    tupla = (letter, frequency / total_characters)
    print(tupla)
