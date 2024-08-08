HEADER_HACKERZELT = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'de',
    'origin': 'https://reservierung.hacker-festzelt.de',
    'priority': 'u=1, i',
    'referer': 'https://reservierung.hacker-festzelt.de/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-festzelt-os-company': 'FOSHACK943',
}

HEADER_SCHOTTENHAMEL = {
    'Accept': 'application/json',
    'Accept-Language': 'de',
    'Content-Type': 'application/json',
    'Origin': 'https://reservierung.festhalle-schottenhamel.de',
    'Referer': 'https://reservierung.festhalle-schottenhamel.de/register/1',
    'Sec-Fetch-Mode': 'cors',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'X-Festzelt-Os-Company': 'KDLWJDR',
    'access-control-request-headers': 'content-type,x-airlst-company'
}

HEADER_SCHUETZENZELT = {
    'authority': 'api.schuetzenfestzelt.wiesn-os.de',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': 'application/json',
    'sec-fetch-dest': 'empty',
    'accept-language': 'de',
    'X-Festzelt-Os-Company': 'M5RN1H1',
    'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
    'content-type': 'application/json',
    'origin': 'https://reservierung.schuetzenfestzelt.com',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'referer': 'https://reservierung.schuetzenfestzelt.com/register/1',
}

BASE_URL_HACKERZELT = "https://api.festzelt-os.com/lp/guestlists"
BASE_URL_SCHOTTENHAMEL = "https://api.schottenhamel.wiesn.airlst.com/lp/guestlists"
BASE_URL_SCHUETZENZELT = "https://api.schuetzenfestzelt.wiesn-os.de/lp/guestlists"
