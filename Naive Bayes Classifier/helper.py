import re
import string

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer

def clean_text(text, stop_words, stemmer):
    '''
    Input:
        text: a string containing text
    Output:
        clean_text: a list of words containing the processed text

    '''
    
    #remove punctuations
    text = re.sub(r'[^\w\s]', '', text)
    tokenizer = TweetTokenizer()
    tweet_tokens = tokenizer.tokenize(text)
    
    clean_text=[]
    for word in tweet_tokens:
        if (word not in stop_words): # remove stopwords
            stem_word=stemmer.stem(word)  # stemming word
            clean_text.append(stem_word)
    return clean_text


def find_freq(vocab,word,label):
    '''
    Input:
        vocab: a dictionary with the frequency of each tuple(word,label)
        word: the word to look up
        label: the label corresponding to the word
    Output:
        n: the number of times(freqency) the word with the given label appears
    '''
    if((word,label) in vocab):
        n=vocab[(word,label)]
    else:
        n=0        
    return n


def word_sentiment(vocab):
    '''
    Input:
        freqs: a dictionary with the frequency of each tuple
    Output:
        (pos_words,neutr_words,neg_words): To get individual lists of positive, negative and neutral words
    '''
    pos_words=[]
    neg_words=[]
    neutr_words=[]
    
    vocab_words=[key[0] for key in vocab.keys()]

    for word in vocab_words:
        if(find_freq(vocab,word,0)!=0):
            neutr_words.append(word)
        elif(find_freq(vocab,word,-1)!=0):
            neg_words.append(word)
        elif(find_freq(vocab,word,1)!=0):
            pos_words.append(word)
    return (pos_words,neutr_words,neg_words)


