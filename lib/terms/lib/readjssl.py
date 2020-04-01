import re
# file returns a function which takes file object containing jssl and spits out the pythonified version of that data

def Chew_JSSL (jssl_file, tuples=False):
    '''
    input  --> file name [tuples]
    output --> [{},], [[(),],]
    '''
    #this is going to be fun
    #lets hope this works
    
    #get the lines
    content = jssl_file.readlines()
    content = [x.strip() for x in content]

    #remove everything that isn't a triple hyphen or key:value
    legal = re.compile("^((---)|([^:]*:[^:]*))$");
    content = [x for x in content if re.match(legal, x)]

    #get indicies of the triple hyhens
    hyphens = [i for i, x in enumerate(content) if x == '---']

    #remove the index for an unmatched triple hyphen
    hyphens = hyphens[0:len(hyphens) - (len(hyphens)%2)] 

    #create the list of lists
    data = []

    #hyphens iterator object
    hyphiter = iter(hyphens)
    for x in hyphiter:
        #list from space after first hyphen to last hyphen
        pairs=[(pair[0:pair.index(':')],pair[pair.index(':')+1:len(pair)]) for pair in content[x+1: next(hyphiter)]]
        if not tuples:
            data.append(dict(pairs))
        else:
            data.append(pairs)
    return data 


def Spit_JSSL (data):
    '''
    input -->  list of dictionaries
    output --> valid JSSL
    '''
    #the immitted string is the spit
    spit = ''
    for JSSLL in data:
        spit+='---\n'
        keys = list(JSSLL.keys())
        for key in keys:
            spit+= f"{key}:{JSSLL[key]}\n"
        spit+='---\n'
    return spit;
        
    

    
    











    
