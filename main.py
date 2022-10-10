import requests
from bs4 import BeautifulSoup

url = 'https://finance.rambler.ru/currencies/'

def currencyAMD(a):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    quites = soup.find('a', {'href': '/currencies/AMD/'}).text
    quites = quites.replace('\n', ' ')
    quites = quites.split('  ')[4]
    if a>0:
        return(str(float(quites)/1000*a))
    else:
        return 0

def currencyAUD(a):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    quites = soup.find('a', {'href': '/currencies/AUD/'}).text
    quites = quites.replace('\n', ' ')
    quites = quites.split('  ')[4]
    if a>0:
        return(str(float(quites)*a))
    else:
        return 0


def currencyBYN(a):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    quites = soup.find('a', {'href': '/currencies/BYN/'}).text
    quites = quites.replace('\n', ' ')
    quites = quites.split('  ')[4]
    if a > 0:
        return (str(float(quites) * a))
    else:
        return 0


def currencyDKK(a):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    quites = soup.find('a', {'href': '/currencies/DKK/'}).text
    quites = quites.replace('\n', ' ')
    quites = quites.split('  ')[4]
    if a > 0:
        return (str(float(quites) * a))
    else:
        return 0

def currencyUSD(a):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    quites = soup.find('a', {'href': '/currencies/exchange/?utm_medium=widget'}).text
    quites = quites.replace('\n', ' ')
    quites = quites.split('  ')[8]
    if a > 0:
        return (str(float(quites) * a))
    else:
        return 0

def currencyEUR(a):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    quites = soup.find('a', {'href': '/currencies/exchange/?utm_medium=widget'}).text
    quites = quites.replace('\n', ' ')
    quites = quites.split('  ')[15]
    if a > 0:
        return (str(float(quites) * a))
    else:
        return 0

def currencyAMDT():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    quites = soup.find('a', {'href': '/currencies/AMD/'}).text
    quites = quites.replace('\n', ' ')
    quites = quites.split('  ')
    number = quites[4]
    prozhent = quites[5]
    plus_or_minus = prozhent[1]
    prozhent = prozhent[2::]
    if plus_or_minus == '+':
        result = float(number)+(float(number)/100*float(prozhent))
    elif plus_or_minus == '-':
        result = float(number) - (float(number) / 100 * float(prozhent))
    return(str(result/1000))

def currencyAUDT():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    quites = soup.find('a', {'href': '/currencies/AUD/'}).text
    quites = quites.replace('\n', ' ')
    quites = quites.split('  ')
    number = quites[4]
    prozhent = quites[5]
    plus_or_minus = prozhent[1]
    prozhent = prozhent[2::]
    if plus_or_minus == '+':
        result = float(number) + (float(number) / 100 * float(prozhent))
    elif plus_or_minus == '-':
        result = float(number) - (float(number) / 100 * float(prozhent))
    return(str(result))


def currencyBYNT():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    quites = soup.find('a', {'href': '/currencies/BYN/'}).text
    quites = quites.replace('\n', ' ')
    quites = quites.split('  ')
    number = quites[4]
    prozhent = quites[5]
    plus_or_minus = prozhent[1]
    prozhent = prozhent[2::]
    if plus_or_minus == '+':
        result = float(number) + (float(number) / 100 * float(prozhent))
    elif plus_or_minus == '-':
        result = float(number) - (float(number) / 100 * float(prozhent))
    return(str(result))


def currencyDKKT():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    quites = soup.find('a', {'href': '/currencies/DKK/'}).text
    quites = quites.replace('\n', ' ')
    quites = quites.split('  ')
    number = quites[4]
    prozhent = quites[5]
    plus_or_minus = prozhent[1]
    prozhent = prozhent[2::]
    if plus_or_minus == '+':
        result = float(number) + (float(number) / 100 * float(prozhent))
    elif plus_or_minus == '-':
        result = float(number) - (float(number) / 100 * float(prozhent))
    return(str(result))

def currencyUSDT():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    quites = soup.find('a', {'href': '/currencies/USD/?utm_medium=widget'}).text
    quites = quites.replace('\n', ' ')
    quites = quites.split('  ')
    prozhent = quites[5]
    number = quites[1]
    plus_or_minus = prozhent[0]
    prozhent = prozhent[1::]
    if plus_or_minus == '+':
        result = float(number) + (float(number) / 100 * float(prozhent))
    elif plus_or_minus == '-':
        result = float(number) - (float(number) / 100 * float(prozhent))
    return(str(result))

def currencyEURT():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    quites = soup.find('a', {'href': '/currencies/EUR/?utm_medium=widget'}).text
    quites = quites.replace('\n', ' ')
    quites = quites.split('  ')
    prozhent = quites[5]
    number = quites[1]
    plus_or_minus = prozhent[0]
    prozhent = prozhent[1::]
    if plus_or_minus == '+':
        result = float(number) + (float(number) / 100 * float(prozhent))
    elif plus_or_minus == '-':
        result = float(number) - (float(number) / 100 * float(prozhent))
    return(str(result))

# currencyAMD()
# currencyAUD()
# currencyBYN()
# currencyDKK()
# currencyUSD()
# currencyEUR()
# currencyAMDT()
# currencyAUDT()
# currencyBYNT()
# currencyDKKT()
# currencyUSDT()
# currencyEURT()