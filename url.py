import string
import random

class URLShortener:
    def __init__(self):
        self.url_to_shortcode = {}
        self.shortcode_to_url = {}
        self.allowed_chars = string.ascii_letters + string.digits
        self.shortcode_length = 7

    def shorten_url(self, original_url):
        if original_url in self.url_to_shortcode:
            return self.url_to_shortcode[original_url]

        shortcode = self.generate_shortcode()
        self.url_to_shortcode[original_url] = shortcode
        self.shortcode_to_url[shortcode] = original_url
        return shortcode

    def generate_shortcode(self):
        while True:
            shortcode = ''.join(random.choice(self.allowed_chars) for _ in range(self.shortcode_length))
            if shortcode not in self.shortcode_to_url:
                return shortcode

    def restore_url(self, shortcode):
        if shortcode in self.shortcode_to_url:
            return self.shortcode_to_url[shortcode]
        else:
            return None

url_shortener = URLShortener()
original_url = input("Enter the URL to shorten: ")
shortened_url = url_shortener.shorten_url(original_url)
print("Shortened URL:", shortened_url)

shortcode = input("Enter the shortcode to restore the original URL: ")

original_url = url_shortener.restore_url(shortcode)
print("Original URL:", original_url)
