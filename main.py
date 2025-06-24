'''
Paste the generated text file content on your browser.
'''



url_end = input("Enter your domain name--> ")

#There are many url which support this, it just tricks user. STAY SAFE!

url = f"https://accounts.google.com+signin=secure+v2+identifier=passive@{url_end}"

with open("url.txt", "w") as f: #it will create a file and save the content simple

    data = f.write(url)


