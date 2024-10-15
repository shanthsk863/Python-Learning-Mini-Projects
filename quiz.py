print("Wll come to the Quiz Game ")
user =input('Do  you want to play the Quiz?  ').lower()
count = 0
if user =='yes':
    print("Lets Play :)",'\n')
    print("The quations are  : ")

    user = input('What is the full form of RAM? ').lower()
    if user == 'random access memory':
        print('Correct! ')
        count+=1
    else:
        print('Incorrect!')     

    user = input('What is the full form of CPU? ').lower()
    if user == 'cental prossessing unit':
        print('Correct! ')
        count+=1
    else:
        print('Incorrect!')    

    user = input('What is the fulll form of ROM? ').lower()
    if user == 'read only memory':
        print('Correct!')
        count+=1
    else:
        print('Incorrect!')   

else:
    print("Thanks for the reesponse")    

print(f'Total correct ans are :{count}', 'Out of 3 quations ')
user = input('Do you want to the scores in % format ? ').lower()
if user =='yes':
    print(f'Total Score is : {count*3/100}')
