import random
from secret import flag

laws = [
    'A robot may not injure a human being or, through inaction, allow a human being to come to harm.',
    'A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.',
    'A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.'
]

sentences = [
    ['What', 'is', 'the', 'First', 'law', 'of', 'robotics', '?'],
    ['Can', 'you', 'tell', 'me', 'the', 'Second', 'law', '?'],
    ['Give', 'me', 'the', 'Third', '!']
]

art = '''
__________      ___.           __    ___________              __                       
\______   \ ____\_ |__   _____/  |_  \_   _____/____    _____/  |_  ___________ ___.__.
 |       _//  _ \| __ \ /  _ \   __\  |    __) \__  \ _/ ___\   __\/  _ \_  __ <   |  |
 |    |   (  <_> ) \_\ (  <_> )  |    |     \   / __ \\  \___|  | (  <_> )  | \/\___  |
 |____|_  /\____/|___  /\____/|__|    \___  /  (____  /\___  >__|  \____/|__|   / ____|
        \/           \/                   \/        \/     \/                   \/  
'''

print("")
print("Welcome to the Solaria's Robot Factory!")
print("We are proud to provide you with the best robots in the galaxy.")
print(art)
print("")
print("Before the robots can be shipped, we need to teach them the Three Laws of Robotics.")
print("Can you help us out?")
print("(N.B.: The robots are still learning to speak, so their sentences may be a bit broken.)")
print("")
print("")



for i in range(100):
    ran = random.randint(0, 2)
    # join the word in a random way
    print(" ".join(random.sample(sentences[ran], len(sentences[ran]))))
    input_law = input()
    print("")
    if input_law != laws[ran]:
        print("Nope, that's not right.")
        exit(1)


print(flag)
exit(0)