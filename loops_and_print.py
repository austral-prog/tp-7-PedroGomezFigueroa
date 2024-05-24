def enumerate_list(list):
    x=[]
    for i in list:
        if i != "":
            x+=  [f"{len (x)}. {i}"]
    return x


def enumerate_backwards(list):
    x=[]
    for i in list:
        if i != "":
            x+=  [f"{len (x)}. {i[::-1]}"]  
    return x
