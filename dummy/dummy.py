
def prompt(text:str) -> str:
    #first we read our text from corpus.txt file 
    try:
        with open("././corpus.txt", r, encoding='utf-8') as file:
            text=file.read()
            #Then we split the text into words using an empty space as the delimeter
            # we also convert all the words and our token to lower case
            words = text.lower.split()
            token = token.lower()
            #count the number of instances the word appears in the text
            no_of_word_instances = words.count(token)
            
            #formulate and return our prompt
            return(f"The term {token} shows up in the corpus {no_of_word_instances} times")
    except FileNotFoundError:
        print("File not found")



    
