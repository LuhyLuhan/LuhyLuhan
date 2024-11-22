from microbit import*
import random
user = "nothing"
t = 500
names = ["luhan","rocco"]
keywords = []
responses = []
introduction = ['Hi what is your name? ']
outro = ["Have a nice day "]
intro = input(random.choice(introduction))
intro = intro.lower()
for name in range(len(names)):
    nam = False
    
    if (names[name] in intro):
        print("Welcome back " + names[name])
        nam = True
        break
    if nam == False:
        print("Nice to meet you " + intro)
        name = intro.lower()
        names.append(name)
print("Press button A")
#This loop will run until the a.i. has noticed a bye a sentance:
while user != "bye":
    keywords_found = False
    b = button_a.is_pressed()
    if b:
        user = input("Type a sentance (or type bye to quit)")
        user = user.lower()
        sleep(t)
        #These for loops and if statements are used to see if the a.i. knows that word:
        for index in range(len(keywords)):
            if (keywords[index] in user):
                print(responses[index])
                keywords_found = True
                print("press button A")
    
    
        if keywords_found == False:
            new_keyword = input("I'm not sure how to respond. What keyword should i respond to?")
            new_keyword = new_keyword.lower()
            keywords.append(new_keyword)
            new_response = input("How should I respond to " + new_keyword + '?')
            responses.append(new_response)
            print("Press button A")
print(outro)