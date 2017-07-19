import re
from tinder.models.user import User
from tinder.models.base import Model

facebook_id_pattern = re.compile(u'\.com/(\d+?)/')


class Friend(Model):

    def __init__(self, data, session):
        """
        Classe para criar um link entre o perfil do Tinder com a conta do facebook
        """
        self._session = session
        self._data = data
        self.name = data['name']
        self.user_id = data['user_id']
        self.in_squad = data['in_squad']

        # Extrai o id do facebook.
        try:
            processed_files = data['photo'][0]['processedFiles']
            facebook_graph_url = processed_files[0]['url']
            self.facebook_id = re.\
                search(facebook_id_pattern, facebook_graph_url).group(1)

            # Create facebook profile link.
            base_url = "https://www.facebook.com/{}"
            self.facebook_link = base_url.format(self.facebook_id)

        except Exception:
            self.facebook_id = None
            self.facebook_link = None

    def get_tinder_information(self):
        """
        Busca as informações no perfil do tinder
        """
        data = self._session._api.user_info(self._data['user_id'])
        return User(data['results'], self._session)

    def __repr__(self):
        return u"{} (fb:{}, ti:{})".format(self.name, self.facebook_id,
                                           self.user_id)
