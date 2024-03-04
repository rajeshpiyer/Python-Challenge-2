 #Write a function that takes a sentence as input and returns a new sentence 
# with the words reversed, while keeping the order of the words in the 
# sentence.

def reverse():
    print("-- Reverse letters of words in a sentence --")
    sentence = input("Enter a sentence : ")
    words = sentence.split(" ")
    reverse_words = []
    for i in words:
        reverse_words.append(i[::-1])
    reverse_sentence = ""
    for i in reverse_words:
        reverse_sentence+=(i+" ")
    print("Reverse Sentence : ",reverse_sentence)

ch='y'
while(ch=='y' or ch=='Y'):
    reverse()
    ch=input("Wish to enter another sentence?(Y/N) : ")


        
    