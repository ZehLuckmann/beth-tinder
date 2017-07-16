#encoding: utf-8
#!/usr/bin/env python
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import logging

class Intention(object):
    """A classe Intention é responsável por retornar a intenção
    de uma frase, positiva ou negativa. Utilizando a classificação
    de acordo com o teorema de Bayes

    Exemplos:
    Entrada: Eu te adoro -> Saída: positivo
    Entrada: Eu te odeio -> Saída: negativo
    """
    def __init__(self):
        """
        Construtor da classe

        cl -> Armazena o classificador
        accuracy -> Armazena a precisão do algoritmo
        """
        self.__cl = None
        self.__accuracy = 0


    def train(self, train_set):
        """
        Treina com a lista de informações formada de frases e suas
        respectivas classificações:

        Exemplo de entrada:
        [('Ótima pergunta','positivo'),('A festa está péssima','negativo')]
        """

        logging.debug('Inicia treinamento da previsão de intenção')
        self.__cl = NaiveBayesClassifier(train_set)
        logging.debug('Treinamento da previsão de intenção finalizado')

    def test(self, test_set):
        """
        Realiza testes com a lista de informações formada
        de frases e sua respectiva classificação para obter a precisão:

        Exemplo de entrada:
        [('Ótima linguagem', 'positivo'),('Péssima essa linguagem', 'negativo')]
        """

        logging.debug('Inicia teste da previsão de intenção')
        self.__accuracy = self.__cl.accuracy(test_set)
        logging.debug('Teste da previsão de intenção finalizado')
        logging.info('Precisão da previsão: {}'.format(self.__accuracy))

    def return_intention(self, phrase):
        """
        Retorna a intenção da frase de acordo com o classificador criado

        Exemplo de entrada:
        'Eu estou com muita raiva'
        Exemplo de saída:
        'A frase "Eu estou com muita raiva" é de caráter: negativo'
        """
        logging.debug('Analisa a frase "{}"'.format(phrase))
        blob = TextBlob(phrase,classifier=self.__cl)
        return 'A frase "{}" é de caráter: {}'.format(phrase, blob.classify())
