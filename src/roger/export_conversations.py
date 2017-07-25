import tinder.utils
import logging
import roger.manage_files

def start():

    logging.debug("Busca conversas")
    conversations = tinder.utils.get_conversations()
    logging.debug("Busca de conversas finalizada")

    result = []
    for conversation in conversations:

        aux = ""
        aux2 = ""
        talker = ""

        for talk in conversation:
            if talker == talk[0]:
                aux += " {br} " + remove_commas(talk[1])
            else:
                if aux2 != '' and aux != '':
                    result.append([aux2, aux])

                aux2 = aux
                aux = remove_commas(talk[1])

                talker = talk[0]

    roger.manage_files.write_csv_file('./teste.csv', result)

def remove_commas(texto):
    texto.replace(',', '{cm}')
    return texto
