import sys
print(f"python version::{sys.version}")



def switch(language:str)->str:
    match language:
        case "Java" | "JavaScript":
            return "Hm, Coffee!"
        case "Python":
            return "Snakes"
        case _:
            return "sorry, IDK"
        
print(switch('Python'))
print(switch('Go'))
print(switch("JavaScript"))



symbols = {'F':'\u2192', 'B':'\u2190','L':'\u2191',"R":'\u2193',"pick":'\u2923',"drop":'\u2925'}
print(symbols)


def op(cmd:str)->str:
    match cmd:
        case ["move", ('F'|'B'|'L'|'R') as direction]:
            return symbols[direction]
        case "pick":
            return symbols['pick']
        case 'drop':
            return symbols['drop']
        case _:
            raise ValueError(f"{cmd} cmd invalid")
        


print(op(['move','F']))
print(op('pick'))
print(op('fly'))