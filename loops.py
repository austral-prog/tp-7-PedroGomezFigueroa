def index_of_by_index(word, list, index):

    if(word in list):
        if (list.index(word)>=index):
            return list.index(word)
        else:
            if word in list[index:]:
                return list[index:].index(word) + index
            else:
                return -1
        
    else:
        return -1

def index_of_empty(list):

    if "" in list:
        return list.index("")
    else:
        return -1

def index_of(word, list):
    if word in list:
        return list.index(word)
    else:
        return -1

def put(word, list):
    for i, vacio in enumerate(list):
        if vacio == "":
            list[i] = word
            return i 
    return -1

def remove(word, list):
    iti = 0
    for i, num in enumerate(list):
        if num == word:
            list[i] = ""
            iti +=1

    return iti
