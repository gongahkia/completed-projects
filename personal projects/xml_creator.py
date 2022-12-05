fhand=open('Charlie.xml','w')

#function to handle writing of the opening root element
def root_elemental_opening(input):
    global root_element
    global fhand
    root_element=input1
    fhand.write(f'<{root_element}>\n')

#function to handle writing of the closing root element
def root_elemental_closing():
    global root_element
    global fhand
    fhand.write(f'</{root_element}>')

#function to handle writing of the respective strings and their enclosing elements
def tag_name_content (input, input01):
    global string
    global fhand
    string=input2
    tag_name=input3
    fhand.write(f'<{tag_name}>{string}</{tag_name}>\n')

#the actual program
input1=input('What do you want as your root element?: ')
root_elemental_opening(input1)
indent_count=0
while True:
    input4=input('Do you want to stop? [Y/N]\n')
    if input4.lower()=='y':
        break
    input2=input('Enter the content: ')
    input3=input('Enter tag name for this set of text: ')
    input5=input('[Indent/Unindent/Same]: ')
    if input5.lower()=='indent' or input5.lower()=='i': 
        indent_count=indent_count+1
        for i in range(indent_count):
            fhand.write('\t')
    if input5.lower()=='unindent' or input5.lower()=='u':
        indent_count=indent_count-1
        for x in range(indent_count):
            fhand.write('\t')
    if input5.lower()=='same' or input5.lower()=='s':
        for x in range(indent_count):
            fhand.write('\t')
    tag_name_content(input2,input3)
root_elemental_closing()
fhand.close()
