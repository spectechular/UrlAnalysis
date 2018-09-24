class URL:
    def __init__(self, url_string, malicious):
        self.url_string = url_string
        if malicious == 'bad':
            self.malicious = 1
        else:
            self.malicious = 0

    def print_url_string(self):
        print(self.url_string)

    def get_url_string(self):
        return self.url_string

    def is_malicious(self):
        if self.malicious == 1:
            print("Is Malicious")
        else:
            print("Not Malicious")


