ReadLetters = str(input('please type the phrase')).strip()
#print(ReadLetters.count('a'))
#print(ReadLetters.find('a'))
#print(ReadLetters.find('a'))
print('The letter A appears {} times in the sentence.'.format(ReadLetters.upper().count('A')))
print('The first letter A appeared in the postion {}'.format(ReadLetters.upper().find('A')+1))
print('The last letter A appeared in the postion {}'.format(ReadLetters.upper().rfind('A')+1))

#rfind --> It counts as of the right side of the program


