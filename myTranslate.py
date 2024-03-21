#Student name: Aryan Patel
#Student number: 501029026
#Section: 1

# Reverses the EnglishToFrench dictionary and returns the FrenchToEnglish dictionary
def reverseDictionary(dictionary):
    FtoE = {}  # defines a new dictionary
    for key, value in dictionary.items():  # iterates through the dictionary
        FtoE[value] = key  # the keys become the values and vice versa
    return FtoE

EnglishToFrench = {'dad': 'pere', 'I': 'je', 'my': 'mon', 'to': 'a', 'with': 'avec', 'shop': 'magasiner', 'for': 'pour',
                   'groceries': 'epicerie', 'buy': 'acheter', 'box': 'boite', 'chocolates': 'chocolats', 'of': 'du',
                   'eggs': 'oeufs', 'and': 'et', 'bread': 'pain', 'mom': 'mere', 'one': 'un', 'two': 'deux', 'three':
                   'trois', 'four': 'quatre', 'dozen': 'douzaine', 'egg': 'oeuf', 'like': 'aime', 'list': 'liste',
                   'is': 'est', 'are': 'sont', 'items': 'articles', 'on': 'sur', 'five': 'cinq', 'six': 'six', 'have':
                   'avoir', 'there': 'la', 'seven': 'sept', 'eight': 'huit', 'nine': 'neuf', 'ten': 'dix', 'bag': 'sac',
                   'milk': 'lait', 'love': 'amour', 'bought': 'achete', 'the': 'le', 'yogurt': 'yaourt', 'beef': 'boeuf'
                   ,'fish': 'poisson', 'oil': 'huile', 'cheese': 'fromage', 'carrots': 'carottes', 'tomatoes': 'tomates'
                   ,'mushrooms': 'champignons', 'spinach': 'epinard', 'rice': 'riz', 'friends': 'amis', 'you': 'tu',
                   'My': 'Mon'}

FrenchToEnglish = reverseDictionary(EnglishToFrench)  # the reverse dictionary is created by calling the function

dicts = {'English to French': EnglishToFrench, 'French to English': FrenchToEnglish}

# Translates each word/key to its corresponding value by taking the word and direction as parameters
def translateWord(word, dictionary):
    if word in dictionary.keys():  # checks if the word is a key in the dictionary
        return dictionary[word]  # returns the corresponding value of the key
    elif word != '':  # checks if word is not an empty string
        return "'" + word + "'"  # returns the word that's not in the dictionary with quotations
    else:
        return word

def translate(phrase, dicts, direction):
    LCletters = 'abcdefghijklmnopqrstuvwxyz'
    letters = LCletters + LCletters.upper()  # combines both uppercase and lowercase letters
    dictionary = dicts[direction]  # stores which language is being translated to
    translation = ''
    word = ''
    is_first = True

    for char in phrase:
        if char in letters:
            word += char  # adds the character to word
        else:   # makes first letter of first word always uppercase if word is in dictionary
            if is_first:  # checks if the word is the first word
                first_word = translateWord(word, dictionary) + char  # first word becomes the translated word
                translation += first_word[0].upper() + first_word[1:]  # adds the word into the translated string
                is_first = False
                word = ''  # word is changed back to an empty string
            else:  # translates all the words after the first word if they're in the dictionary
                translation += translateWord(word, dictionary) + char
                word = ''
    translation += translateWord(word, dictionary)  # adds the final word into the translated string
    return translation

def valid_input(n):
    if n == 1:  # checks if user input is '1'
        sentence = input('Enter something in English: ')  # asks user to enter something English
        translated = translate(sentence, dicts, 'English to French')  # calls the translate function and translates
        print('In English:', sentence)  # prints what the user entered in English
        print('In French:', translated) # prints the French translated output
    else:  # the other possible user input has to be '2'
        sentence = input('Enter something in French: ')  # asks user to enter something French
        translated = translate(sentence, dicts, 'French to English')  # calls the translate function and translates
        print('In French:', sentence)     # prints what the user entered in French
        print('In English:', translated)  # prints the English translated output

while True:
    try:  # asks user to enter '1' or '2'
        n = int(input("Enter '1' to translate from English to French\nEnter '2' to translate from French to English "))
    except:  # if user input is not an integer
        print('Invalid input')
    else:
        if n == 1 or n == 2:  # checks if user input is '1' or '2'
            valid_input(n)  # calls function and takes in valid user input as parameter
            break  # breaks while loop
        else:
            print('Invalid input')
























