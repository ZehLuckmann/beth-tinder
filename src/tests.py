# -*- coding: utf-8 -*-
import roger.preprocessing, roger.intention_prediction
train_set = [
    ('Que legal', 'positivo'),
    ('Este lugar é horrível', 'negativo'),
    ('Você é uma pessoa adorável', 'positivo'),
    ('Você é uma pessoa horrível', 'negativo'),
    ('A festa está ótima', 'positivo'),
    ('A festa está péssima', 'negativo'),
    ('Este lugar é maravilhoso', 'positivo'),
    ('Estou cansada disso.', 'negativo'),
    ('Eu te odeio', 'negativo'),
    ('Eu te adoro', 'positivo'),
    ('Eu te amo', 'positivo'),
    ('Você é incrível','positivo'),
    ('Eu estou com muita raiva','negativo'),
    ('Eu odeio esse negócio','negativo'),
    ('Essa menina é fantátisca','positivo'),
    ('Essa dica é muito boa','positivo'),
    ('Que comida gostosa','positivo'),
    ('Que comida horrível','negativo'),
    ('Estou me sentindo ótima','positivo'),
    ('Hoje eu estou péssima','negativo'),
    ('Eu não odeio todo mundo', 'positivo')
]

test_set = [
    ('Ótima pergunta', 'positivo'),
    ('Péssima essa pergunda', 'negativo'),
    ('Você é horrível', 'negativo'),
    ('Comida gostosa!', 'positivo'),
    ('Que raiva!', 'negativo'),
    ('Ótima festa!', 'positivo'),
    ('Eu odeio todo mundo','negativo')
]

#train_set = roger_preprocessing.general_treatments(train_set)
#test_set = roger_preprocessing.general_treatments(test_set)

#train_set = roger_preprocessing.remove_punctuation(train_set)
#test_set = roger_preprocessing.remove_punctuation(test_set)

roger.intention_prediction.train(train_set, test_set)

print("\nTesta frases:\n")

roger.intention_prediction.print_intention('Eu não odeio todo mundo')
roger.intention_prediction.print_intention('Fiquei cansada desta festa')
