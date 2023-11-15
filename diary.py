# File: lib/diary.py

def make_snippet(string):
    #word = string[:5]
    #word = string.split()[:5]
    word = ' '.join(string.split()[:5])
    sp = len(string.split())

    if sp <= 5:
        return word
    elif sp > 5:
        return word + "..."
    


    #else:
    #    return word + "..."
    
