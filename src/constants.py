HEADER_HACKERZELT = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en,en-US;q=0.7,de;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'hacker-festzelt.de',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}

HEADER_SCHOTTENHAMEL = {
    'Accept': 'application/json',
    'Accept-Language': 'de',
    'Content-Type': 'application/json',
    'Origin': 'https://reservierung.festhalle-schottenhamel.de',
    'Referer': 'https://reservierung.festhalle-schottenhamel.de/register/1',
    'Sec-Fetch-Mode': 'cors',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'X-Airlst-Company': 'KDLWJDR',
    'access-control-request-headers': 'content-type,x-airlst-company'
}

HEADER_SCHUETZENZELT = {
    'authority': 'api.schuetzenfestzelt.wiesn-os.de',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': 'application/json',
    'sec-fetch-dest': 'empty',
    'accept-language': 'de',
    'x-airlst-company': 'M5RN1H1',
    'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
    'content-type': 'application/json',
    'origin': 'https://reservierung.schuetzenfestzelt.com',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'referer': 'https://reservierung.schuetzenfestzelt.com/register/1',
}

BASE_URL_HACKERZELT = "https://hacker-festzelt.de/php/hackerformv4.php"
BASE_URL_SCHOTTENHAMEL = "https://api.schottenhamel.wiesn.airlst.com/lp/guestlists"
BASE_URL_SCHUETZENZELT = "https://api.schuetzenfestzelt.wiesn-os.de/lp/guestlists"

TENTMAP_SCHOTTENHAMEL = "[Schottenhamel TentMap](https://www.festhalle-schottenhamel.de/application/files/5915/7616/3902/Zeltplan_2020.jpg)"
TENTMAP_SCHUETZENZELT = "[Schützenzelt TentMap](https://reservierung.schuetzenfestzelt.com/_nuxt/img/tent-map.c61a8f9.png)"

SESSION_STORAGE = 'data/vacancies.json'
