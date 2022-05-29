
import random
import time
inventory = []
items = []

def goodending():
    print('Po zacieklej walce ualo ci sie poslac krola zaglady na wieczny spoczynek')
    time.sleep(5)
    print('Ksiezniczka rzuca ci sie w ramiona i dziekuje za ratunek')
    gold = random.randint(1000, 5000)
    inventory.append(gold)
    time.sleep(5)
    print('Krol Haren ofiaruje ci gore zlota, oraz reke swojej corki')
    time.sleep(5)
    print('KONIEC')

def badending():
    print('Klekasz przed "Doom Lordem". Po chwili czujesz jak jego zimne ostrze przebija twoje serce')
    time.sleep(5)
    print('Ostatnie co slyszysz przed swoja smiercia to smiech twojego oprawcy')
    time.sleep(5)
    print('KONIEC')


def zamek():
    print('Docierasz na najwyzsze piertro zamku')
    time.sleep(3)
    print('Dostrzegasz "Doom Lorda" ktory siedzi na tronie, a za nim zamknieta w klatce ksiezniczke')
    time.sleep(3)
    print('Witaj czekalem na ciebie wojowniku')
    time.sleep(3)
    print('Mam dla ciebie propozycje. Stan u mojego boku, a obiecuje ci ze razem bedziemy rzadzic tym krolestwem')
    time.sleep(5)
    print('Lub zgin jak cala reszta')
    answer = input('Walcz-->1,Przyjmij propozycje-->2')
    if answer == '1':
        print(goodending())
    elif answer == '2':
        print(badending())



def polnoc():
    print('Docierasz pod brame zamku. Przed wejsciem zauwazasz nieumarlego maga')
    time.sleep(4)
    print('Mag zwraca sie do ciebie "Jesli odgadniesz moja zagadke, bedziesz mogl przjesc. Jesli nie zostaniesz przeniesiony zpowrotem do miasta"')
    time.sleep(4)
    answer = input("Zawsze przyjdzie, ale nigdy nie przyjdzie dzisiaj. Co to takiego?")
    if answer == 'jutro':
        print('Dobrze, mozesz isc dalej')
        zamek()
    else:
        print('Zla odpowiedz')
        print('Mag przenosi cie z powrotem do miasta')
        centrum()

def wrozbitka():
    print('Docierasz do namiotu starej wrozbitki ktora oferuje ci wrozbe')
    wrozba1 = 'Bedziesz wiodl dlugie i szczesliwe zycie'
    wrozba2 = 'W ciagu najblizszych 3 lat zachorujesz na smiertelna chorobe'
    wrozba3 = 'Pisane ci jest zostac wielkim czlowiekiem'
    wrozby = [wrozba1,wrozba2,wrozba3]
    answer = input('Czy zechcesz abym ci wywrozyla? Tak-->1 Nie-->2')
    if answer == '1':
       result = random.choice(wrozby)
       print(result)
       time.sleep(2)
       centrum()
    elif answer == '2':
      print('W takmi razie zegnaj')
      centrum()




def gobliny():
    gold = random.randint(5, 50)
    print('Po zacieklej walce z goblinskim plemieniem zdobywasz')
    sum_result = sum(inventory)
    inventory.append(gold)
    print(sum_result)
    print('Zlotych monet, po czym wracasz do miasta')
    time.sleep(2)
    centrum()

def centrum():
 print('Znajdujesz sie w centrum miasta. Zachod--> Gobliny-1, Wschod--> Wrozbitka-2, Polnoc--> Droga do zamku-3 ')
 answer = input('Gdzie chcesz isc?')
 if answer == '1':
  print(gobliny())
 elif answer == '2':
  print(wrozbitka())
 elif answer == '3':
  print(polnoc())






print('"DEMON LORD AND THE PRINCESS"')
time.sleep(5)
Name = input('Wpisz imie swojego wojownika-->')
print('Budzisz sie w karczmie.Ostatnio doszly cie sluchy ze w zamku na polnocy zly "DEMON LORD" porwal kiezniczke Anastasie ')
time.sleep(5)
print('Krol Haren obiecal, ze tego ktoremu uda sie odzyskac jego corke obsypie zlotem i odda mu polowe krolestwa ')
time.sleep(5)
print('Jestes doswiadczonym wojownikiem, niestety zdajesz sobie sprawe z tego ze nie bedzie to latwe zadanie')
time.sleep(5)
print('Zwlaszcza ze nie masz przy sobie zlamanego grosza, a na taka wyprawe potrzebne ci bedzie odpowiednie wyposazenie')
time.sleep(5)
print('Chwytasz za swoj pordzewialy miecz i ruszasz w kierunku goblisnkiej osady aby zarobic troche zlotych monet')
time.sleep(5)
centrum()
sum_result = sum(inventory)
print(sum_result)
print('To twoje Zloto na koniec')

