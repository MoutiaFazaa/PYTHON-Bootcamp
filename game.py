import random

#Get Guess
def get_guess():
    return list(input('What is your Guess? =>  '))

#Generate computer code 123
def generate_code():
    digits = [str(num) for num in range(10)]
    #Shuffle the digits
    random.shuffle(digits)
    #then grab the first three
    return digits[:3]

#Generate the clues
def generate_clues(code,user_guess):
    if user_guess == code:
        return "CODE CRACKED!"
    clues = []
    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append('match')
        elif  num in code:
                clues.append('clode')
    if clues == []:
        return ['nope']
    else:
        return clues
        
#Run game logic
print('welcom code breaker!  ')
secret_code = generate_code()
clues_report =[]
while clues_report != 'CODE CRACKED!':
    guess = get_guess()
    clues_report = generate_clues(guess,secret_code)
    print ('here is the result of your guess:  ')
    for clue in clues_report:
        print(clue)