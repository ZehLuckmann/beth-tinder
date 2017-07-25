import tinder
import robobrowser
import re
import getpass

MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; U; en-gb; KFTHWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.16 Safari/535.19"
FB_AUTH = "https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd"


def get_conversations():
    """
    Retorna um array com uma matriz com o nome do usuário na
    primeira coluna e a conversa na segunda
    """
    conversations = []

    facebook_auth_token = get_access_token()

    session = tinder.Session(facebook_auth_token)
    matches = session.matches()

    for m in matches:
        talk = []
        for men in m.messages:
            talk.append([men.sender.name, men.body])

        conversations.append(talk)

    return conversations

def get_access_token():
    s = robobrowser.RoboBrowser(user_agent=MOBILE_USER_AGENT, parser="lxml")
    s.open(FB_AUTH)

    f = s.get_form()

    print('É necessário que você informe seu login do facebook para conectar ao Tinder:')
    email = input('Email: ')
    password = input('Senha: ')

    f["pass"] = password
    f["email"] = email



    access_token = ''
    while access_token == '':
        try:

            s.submit_form(f)

            f = s.get_form()
            s.submit_form(f, submit=f.submit_fields['__CONFIRM__'])
    
            access_token = re.search(r"access_token=([\w\d]+)", s.response.content.decode()).groups()[0]

        except:
            print('Falha ao acessar, tentando novamente')
            acess_token = ''

    return access_token
