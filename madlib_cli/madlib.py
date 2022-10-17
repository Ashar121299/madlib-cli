import re 
def welcoming():
    print("welcome to MADLIB game")
    print("Mad Libs are a word replacment game")
    print("so you will enter some words then it will replaced in a pargraph")
    print("it may be a funny :) ")
    print("let we start")
    
welcoming()


def read_template(path):    
    try:
        with open(path) as file:
            content=file.read()
            return content
    except :
       raise FileNotFoundError("the path is invalid")

def parse_template(sentances):
    inside = re.sub(r"[^{]+(?=})","",sentances)
    language_part=tuple(re.findall(r"[^{]+(?=})",sentances))
    return inside,language_part


def inputs(words) -> str:
    arr=[]
    for word in list(words):
        arr.append(input(f'{word} ==>'))
    return tuple(arr)


def merge(inside , words):
    return inside.format(* words)

if __name__=='__main__':
    def result (pathofTxt):
        cont=read_template(pathofTxt)
        ins,parts=parse_template(cont)
        collect=inputs(parts)
        res=merge( ins , collect)
        return  res
if __name__=='__main__':
    print(result('assets/dark_and_stormy_night_template.txt') )   
 
