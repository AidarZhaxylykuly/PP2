import random
A=random.randint(0, 20)
n=input('Hello! What is your name?')
print('Well, {} I am thinking of a number between 1 and 20.'.format(n))
s=1
for i in range(21):
    k=int(input('Take a guess.'))
    if k > A:
        print("Your guess is too high.")
        s+=1
        continue
    elif k < A:
        print("Your guess is too low.")
        s+=1
        continue
    else:
        print('Good job, {}! You guessed my number in {} guesses!'.format(n, s))
        quit()