import random

def random_nickname():
    adjectives = ['smart','fast','quick','intelligent', 'bright', 'wise', 'brilliant', 'awesome', 'incredible',
                  'studious', 'amazing', 'agile', 'academic', 'sharp', 'inventive', 'genius']

    nouns = ['Bear','Tiger','Frog','Monkey', 'Koala', 'Fox', 'Wolf', 'Cat', 'Bunny', 'Panda', 'Cat' 
             'Zebra', 'Jaguar', 'Dolphin', 'Bee', 'Eagle', 'Mouse', 'Shark', 'Giraffe', 'Dog', 'Alligator']


    return(random.choice(adjectives) + random.choice(nouns) + str(random.randint(1,99)))
