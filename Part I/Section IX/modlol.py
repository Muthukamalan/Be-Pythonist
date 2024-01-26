# This is My Module LOL!!
'''
THis is module docs
'''


import random

print('------ Running {0} ------'.format(__name__))

def pprint_dict(header:str,d:dict):
    print('\n\n-----------------------')
    print('******** {0} ********'.format(header))
    for k,v in d.items():
        print(k,v)
    print('*********************\n\n')

pprint_dict('module.globals',globals())

print('------ End of {0} ------'.format(__name__))


def crazyword(header:str,word:str)->None:
    print('\n\n-----------------------')
    print('******** {0} ********'.format(header))
    print('word:{0}\nword:{1}'.format(word,''.join(random.sample(word,len(word)))))
    print('*********************\n\n')
