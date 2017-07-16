from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

def train(train_set, test_set):
    global cl
    print('Inicia treinamento')
    cl = NaiveBayesClassifier(train_set)
    accuracy = cl.accuracy(test_set)
    print('Treinamento finalizado')
    print('Precisão da previsão:{}'.format(accuracy))

def print_intention(phrase):
    global cl
    blob = TextBlob(phrase,classifier=cl)
    print('A frase "{}" é de caráter:{}'.format(phrase, blob.classify()))
