
# Online Python - IDE, Editor, Compiler, Interpreter

numbers = {
    'first': 31,
    'second': 83329,
    'third': 19293,
    'fourth': 819,
    'fifth': 993,
}
max=0
updatekey=0;
# print(numbers['first'])
# print(numbers['fourth'])
for i in numbers:
    value= numbers[i]
    if(max<value):
        updatekey= i
        max= value
print(updatekey)    
# print(max)   
    
    
    
    