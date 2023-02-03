import requests
from pprint import pprint


class Heroes:

    base_host = 'https://akabab.github.io/superhero-api/api'

    def get_all_heroes(self):

        uri = '/all.json'
        request_url = self.base_host + uri
        response = requests.get(request_url)
        list_of_info = response.json()
        b = 0
        list_of_names = ['Thanos', 'Captain America', 'Hulk']
        intelligence_list = []
        heroes_dict = {}
        for _ in list_of_info:
            # pprint(list_of_info[b]['name'])
            if list_of_info[b]['name'] in list_of_names:
                # print(list_of_info[b]['name'])
                # pprint(list_of_info[b]['powerstats']['intelligence'])
                heroes_dict[list_of_info[b]['powerstats']['intelligence']] = list_of_info[b]['name']
                intelligence_list.append(list_of_info[b]['powerstats']['intelligence'])

            else:
                pass
            b += 1
        intelligence_list.sort(reverse=True)
        print(heroes_dict[intelligence_list[0]])


if __name__ == '__main__':
    he = Heroes()
    he.get_all_heroes()
