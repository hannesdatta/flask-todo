import random

def random_nickname():
    adjectives = ['smart','fast','quick','intelligent',
                  'studious', 'amazing']

    nouns = ['Bear','Tiger','Frog','Monkey']


    return(random.choice(adjectives) + random.choice(nouns) + str(random.randint(1,99)))
