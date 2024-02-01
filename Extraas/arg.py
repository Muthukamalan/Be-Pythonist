import argparse
import sys 


parser = argparse.ArgumentParser(description="Helps to understand argparser module")
parser.add_argument('-f',help='your firstname',type=str,required=False,dest='first_name',default='muthu')
parser.add_argument('-a','--age',help='your age',type=int,required=False)
parser.add_argument('--sq',help='list of numbers to square',nargs='*',type=float)
parser.add_argument('--cu',help='list of numbers to cubes',nargs='+',type=float,required=True) # + represent atleast one 



group = parser.add_mutually_exclusive_group()
group.add_argument('-v','--verbose',help='if you pass flag it"ll take as true else false',action='store_const',const=True,default=False)
group.add_argument('-q','--quit',action='store_true')



args:argparse.Namespace = parser.parse_args(sys.argv[1:])
print(args)


print(args.first_name)
print(args.age)

if args.sq:
    squares = [n**2 for n in args.sq]
    print(squares)
print([n**3 for n in args.cu])

# python arg.py -h
# python arg.py --first_name --age