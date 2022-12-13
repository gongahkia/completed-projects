file_name=input('Enter a file name: ')
fhand=open(file_name,'r')
empty_dictionary={}
for line in fhand:
    stripped_line=line.rstrip().lower()
    words=stripped_line.split()
    for word in words:
        if word.isalpha():
            for letters in word:
                empty_dictionary[letters]=empty_dictionary.get(letters,0)+1
#print(empty_dictionary)
for freq,apha in (sorted(((frequency,alpha) for (alpha,frequency) in empty_dictionary.items()),reverse=True)):
    print(apha,freq)
