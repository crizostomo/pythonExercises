import requests

class searchAddress:

    def __init__(self, post_code):
        post_code = str(post_code)
        if self.post_code_valid(post_code):
            self.post_code = post_code
        else:
            raise ValueError("Post Code Invalid")

    def __str__(self):
        return self.format()


    def post_code_valid(self, post_code):
        if len(post_code) == 8:
            return True
        else:
            return False

    def format(self):
        return "{}-{}".format(self.post_code[:5], self.post_code[5:])

    def access_via_post_code(self):
        url = "https://viacep.com.br/ws/{}/json".format(self.post_code)
        r = requests.get(url)
        data = r.json()
        return (
            data['bairro'],
            data['localidade'],
            data['uf']
        )