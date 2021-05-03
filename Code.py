
def finder(words_list):
    alphabets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_count={}
    for letter in alphabets:
        letter_count[letter]=0
    for word in words_list:
        letter_List=list(word)
        for letter in letter_List:
            if letter in alphabets:
                letter_count[letter]+=1

    letter_total_count=0
    the_letter=""
    print(letter_count)
    for key,value in letter_count.items():
        if(letter_count[key]>letter_total_count):

            letter_total_count=value
            the_letter=key


    return letter_total_count,the_letter

if __name__ == '__main__':
    str="i am sachi shomeeeee."
    word_list=str.split(" ")


    print(finder(word_list))
