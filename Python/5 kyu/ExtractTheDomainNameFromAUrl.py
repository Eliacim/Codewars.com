'''
https://www.codewars.com/kata/514a024011ea4fb54200004b/python

5 kyu Extract the domain name from a URL


Write a function that when given a URL as a string, parses out just the domain
name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"

'''


import re


def domain_name1(url):
    new = re.sub(re.compile('https*://'), '', url)
    new = new.replace('www.', '')
    return new.split('.')[0]


# This was considered the most clever/best practice on Codewars.com
# so simple and efficient
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


print(domain_name("https://google.com"))  # "google")
print(domain_name("http://google.co.jp"))  # "google")
print(domain_name("www.xakep.ru"))  # "xakep")
print(domain_name("https://youtube.com"))  # "youtube")
