


def palindrome(wordstr):
    word=str(wordstr)
    for i in range(len(word)//2):
        if word[i] == word[len(word)-i-1]:
            p=0
        else:
            return False
            break
    return True


        
