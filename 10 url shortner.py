"""
Generates a shortened version of the url given.

"""


import pyshortner

def shorten_url():
  """Prompts user for a URL and shortens it using Bitly."""
  url = input("Enter a URL to shorten: ")
  short_url = pyshortner.bitly.shorten(url)
  print(f"Shortened URL: {short_url}")

if __name__ == "__main__":
  shorten_url()
