from http.cookies import SimpleCookie

URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.45882581640623%2C%22east%22%3A-80.03585218359373%2C%22south%22%3A25.621078067956006%2C%22north%22%3A25.924065538036224%7D%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat1%22:[%22listResults%22]}&requestId=3'

def cookie_parser():
    cookie_string = 'zguid=23|%24740085ff-02de-4b71-b041-7c2f6f6cfd2a; zgsession=1|c0124d82-8602-4e38-9442-e41e10ee5d7b; JSESSIONID=F60308F6862E126CF38D5B2C140D1539; AWSALB=a1uaQfriNc6pR3gBDYN8aT3rzO+1iXadM7/FmorkBaXQNstFXNdki3Y5lqGekNh2HeUzEj9KK8K9LXKmUvFwaiwWJAaTybHXbvSPqiIybx3cN4eXNXO6aVsmmdKS; AWSALBCORS=a1uaQfriNc6pR3gBDYN8aT3rzO+1iXadM7/FmorkBaXQNstFXNdki3Y5lqGekNh2HeUzEj9KK8K9LXKmUvFwaiwWJAaTybHXbvSPqiIybx3cN4eXNXO6aVsmmdKS; search=6|1602920768508%7Crect%3D25.924065538036224%252C-80.03585218359373%252C25.621078067956006%252C-80.45882581640623%26rid%3D12700%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26sort%3Ddays%26z%3D0%26pt%3Dpmf%252Cpf%26fs%3D1%26fr%3D0%26mmm%3D1%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%0912700%09%09%09%09%09%09'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
        
    return cookies