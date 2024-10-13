from microbit import*
import random
s = 500
t = 100
val = 1 
v = 0
v1 = 0
#This is the list for writing sentances:
article = ['the','a']

noun = ['cat','bat','mat','dog','lion','elephant','human','book',
        'lemon','grape','apple','banana','ship','tree','log']

pronoun = ['him','she','they','we','me','I','their','he','her','myself']

adj = ['good','big','small','tiny','huge','collosal','large','expensive',
       'easy','difficult','hard','cold','hot','fast','quick','amazing',
       'green','yellow','blue','red','purple','black','white','brown']

verb = ['sit','walk','talk','sing','run','eat','hit','jog','munch','speak','play','swim']

adverb = ['here','there','mostly','stupedly','far','nowhere','possibly']

other = ['is','are','was','were']

preposition = ['under','behind','below','above','next to','at'
               ,'in','inside','on','after','underneath','with']

conjunction = ['but','and','while','when']

interjection = ['hey!','oh!','ow!','hi!','ouch!','wow!']

who = ['which','who']

asia = ['when','while','where','as','so','if','although']

that = "that"
#This is the part were the a.i. greets you:
names = ["luhan"]
keywords = ['book']
responses = ['I know a lot about books']
introduction = ['Hi what is your name? ','Howdy, you look like a nice person, what is your name? ','Well look at you what is your name? ',
                'Hi there im Kosie what is your name? ']
outro = ["Have a nice day ",'Hope you have a wonderful day ','May you have an amazing day ']
intro = input(random.choice(introduction))
intro = intro.lower()
for name in range(len(names)):
    nam = False
    
    if (names[name] in intro):
        print("Welcome back " + names[name])
        sleep(t)
        nam = True
    if nam == False:
        print("Nice to meet you " + intro)
        name = intro.lower()
        names.append(name)
user = input("Type a noun (or type bye to quit)")
user = user.lower()
user1 = input("Type a second noun")
user1 = user1.lower()
user2 = input("Type a third noun or no which will make me choose a random noun")
user2 = user2.lower()
p = input("Type a preposition or no for a random one")
p = p.lower()
pr = input("Type a second preposition if you want a complex sentance else no")
pr = pr.lower()
#This lists contains all the stuff that it can start a sentance with:
val = [article,preposition,interjection]
val1 = [that,conjunction,who]
#This list will contain all the words for a sentance.
sen = [0,0,0,0,0,0,0,0]
#This will just tell the person using it to press button_A for a sentance:
print("Press button_A for a sentance with the provided words:")
print("Press button_B to change the nouns and prepositons:")
#This loop will run until the a.i. has noticed a bye a sentance:
while True:
    b1 = button_a.is_pressed()
    b2 = button_b.is_pressed()
    #These for loops and if statements are used to see if the a.i. knows that word:
    '''for index in range(len(keywords)):
        if (keywords[index] in user):
            print("Kosie:" + responses[index])
            keywords_found = True
    
    
    if keywords_found == False:
        new_keyword = input("I'm not sure how to respond. What keyword should i respond to?")
        new_keyword = new_keyword.lower()
        keywords.append(new_keyword)
        new_response = input("How should I respond to " + new_keyword + '?')
        responses.append(new_response)'''
    if b2 == 1:
        user = input("Type a noun (or type bye to quit)")
        user = user.lower()
        user1 = input("Type a second noun")
        user1 = user1.lower()
        user2 = input("Type a third noun or no which will make me choose a random noun")
        user2 = user2.lower()
        p = input("Type a preposition or no for a random one")
        p = p.lower()
        pr = input("Type a second preposition if you want a complex sentance else no")
        pr = pr.lower()
    if b1 == 1:
        v = 0
        sent = [0,0,0,0,0,0,0,0,0,0,0,0]
        no = random.choice(val)
        if no == article:
            no = random.choice(article)
            sen[0] = no
            no = random.choice(adj)
            sen[1] = no
            sen[2] = user
            no = random.choice(other)
            sen[3] = no
            sen[4] = p
            no = random.choice(article)
            sen[5] = no
            no = random.choice(adj)
            sen[6] = no
            sen[7] = user1
            print(' '.join(sen))
            sleep(s)
        if no == preposition:
            sent[0] = p
            no = random.choice(article)
            sent[1] = no
            sent[2] = user
            no = random.choice(other)
            sent[3] = no
            no = random.choice(article)
            sent[4] = no
            sent[5] = user1
            if pr == "no":
                for x in range(6):
                    sent.remove(0)
                print(' '.join(sent))
                sleep(s)
            else:
                v = 1
                if v == 1:
                    no = random.choice(val1)
                    if no == conjunction:
                        no = random.choice(conjunction)
                        sent.append(no)
                    elif no == who:
                        no = random.choice(who)
                        no = ',' + no
                        sent.append(no)
                    else:
                        sent.append(no)
                    no = random.choice(other)
                    sent.append(no)
                    no = random.choice(verb)
                    no = no + "ing"
                    sent.append(no)
                    sent.append(pr)
                    no = random.choice(article)
                    sent.append(no)
                    if user2 == 'no':
                        no = random.choice(noun)
                        sent.append(no)
                    else:
                        sent.append(user2)
                    for x in range(6):
                        sent.remove(0)
                    print(' '.join(sent))
                    sleep(s)
        if no == interjection:
            no = random.choice(interjection)
            sen[0] = no
print(random.choice(outro) + intro)