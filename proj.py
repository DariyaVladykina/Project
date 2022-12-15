from pymorphy2 import MorphAnalyzer
from nltk.tokenize import WordPunctTokenizer

ma = MorphAnalyzer()
wpt = WordPunctTokenizer()

print(ma.parse('Даша'))
#[Parse(word='даша', tag=OpencorporaTag('NOUN,anim,femn,Name sing,nomn'), normal_form='даша', score=1.0, methods_stack=((DictionaryAnalyzer(), 'даша', 1307, 0),))] - результат
a_text = open('a_text.txt','r', encoding='utf-8').read()

for word in wpt.tokenize(a_text):
    # перебираем все "слова" - объекты морфологического анализа
    parsed = ma.parse(word)[0] 
    # parsed - "объект" морфологического анализа
    if 'Geox' in parsed.tag.grammemes:
        # проверяем, содержит ли "объект" признак топонима
        print(word)
  
from requests import get
from bs4 import BeautifulSoup

from time import sleep              # это библиотеки для "скрытной" работы
from random import random, choice   
from user_agents import parse  

URL = "https://www.rulit.me/books/filellin-s-razdeleniem-na-glavy-read-647000-%s.html"
# общий вид URL

the_text = ""
# здесь будет собран текст произведения

for n in range(1,6):    # в романе 120 страниц, но я возьму первые 5
    sleep(random()*5)     # задержка
    print(URL % n)        # подстановка номера "страницы"
    x = get(
        URL % n,
		headers={'user-agent': choice('seq'),},
        timeout=5
    ).content             # создание интернет-запроса
    soup = BeautifulSoup(x, 'lxml') # создание DOM-модели документа
    article = soup('article',{'class':'single-blog'})[0] # выделение объекта в котором текст
    
    a_text = article.text    # получение текста страницы
    the_text += " " + a_text # сборка текста из страниц
    
print(the_text) #текст видно в консоли

for word in wpt.tokenize(the_text):
    parsed = ma.parse(word)[0] 
    if 'Geox' in parsed.tag.grammemes:
        print(word)
# получили топонимы из текста романа