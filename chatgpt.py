import io
import random
import string
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True)
nltk.download('punkt')
nltk.download('wordnet')
f = open(r'C:\Users\USER\Desktop\rithika.txt', errors='ignore')
raw = f.read()
raw = raw.lower()
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)
lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREETING_INPUTS = ("hello", "hi", "greetings", "ssup", "hola", "namasthe", "wassup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello!!", "Hi! nice to meet you."]
ADDITIONAL_GREETINGS = ("how are you", "what's up", "good morning", "good afternoon", "good evening")
ADDITIONAL_RESPONSES = ["I'm doing well, thank you!", "Not much, just chatting. How about you?", "Good " + ur_response.split()[-1] + "!"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def advanced_greeting(sentence):
    for word in sentence.split():
        if word.lower() in ADDITIONAL_GREETINGS:
            return random.choice(ADDITIONAL_RESPONSES)

def response(ur_response):
    r_response = ''
    sent_tokens.append(ur_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        r_response = r_response + "I am sorry! I don't understand you :("
        return r_response
    else:
        r_response = r_response + sent_tokens[idx]
        return r_response

flag = True
print("ChatBot: My name is Sahrutha Reddy. I will answer your queries. If you want to exit, type Bye!")
while flag:
    ur_response = input()
    ur_response = ur_response.lower()

    if ur_response != 'bye':
        if ur_response == 'thanks' or ur_response == 'thank you':
            flag = False
            print("Sahrutha Reddy : You're welcome!")
        else:
            greeting_response = greeting(ur_response)
            if greeting_response is not None:
                print("Sahrutha Reddy : " + greeting_response)
            else:
                advanced_greeting_response = advanced_greeting(ur_response)
                if advanced_greeting_response is not None:
                    print("Sahrutha Reddy : " + advanced_greeting_response)
                else:
                    print("Sahrutha Reddy: ", end="")
                    print(response(ur_response))
                    sent_tokens.remove(ur_response)
    else:
        flag = False
        print("Sahrutha Reddy : Bye! Take care.")

