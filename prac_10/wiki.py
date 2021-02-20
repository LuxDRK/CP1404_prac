import wikipedia


keyword = input('Please input your keywords:\n')
while keyword != '':
    page = wikipedia.page(keyword)
    print(page.title)
    print(page.summary)
    print(page.url)
    keyword = input('Please input your keywords:\n')
