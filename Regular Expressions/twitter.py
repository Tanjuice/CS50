import re


url = input("URL: ").strip()

# username = url.removeprefix("https://twitter.com/")


username = re.sub(r"https://twitter.com/", "", url)

print(f"Username: {username}")