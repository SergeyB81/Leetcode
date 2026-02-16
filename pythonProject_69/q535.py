import hashlib

class Codec:

    def __init__(self):
        self.url_db = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        shortUrl = hashlib.sha1(longUrl.encode('utf-8')).hexdigest()[:6]
        self.url_db[shortUrl] = longUrl

        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url_db[shortUrl]

if __name__ == '__main__':
    c = Codec()
    url1 = 'adfgh'
    url2 = 'mfvlfm;lvmsl;c,c;la dlc'
    shorten1 = c.encode(url1)
    print(shorten1)
    original1 = c.decode(shorten1)
    print(original1)

    print()

    shorten2 = c.encode(url2)
    print(shorten2)
    original2 = c.decode(shorten2)
    print(original2)

#rep5