from random import random
from webcon.common.models import Country, Address

hotel_names = file('hotele-ok.txt').read().split("\n")
streets = file('ulice-ok.txt').read().split("\n")
cities = file('miasta-ok.txt').read().split("\n")
firstnames = file('imiona-ok.txt').read().split("\n")
lastnames = file('nazwiska-ok.txt').read().split("\n")
conf_names = file('konferencje-ok.txt').read().split("\n")

countries = Country.objects.all()

def get_zipcode():
    return "%i%i-%i%i%i" % ((int)(random() * 10), (int)(random() * 10), (int)(random() * 10), (int)(random() * 10), (int)(random() * 10))

#def get_hotel_name():
#    return hotel_names[(int)(random() * len(hotel_names))]

def get_hotel_desc(hotel_name):
    tpl = """Nowoczesny, doskonale zlokalizowany, zmodernizowany {{hotel}} stanowi idealne rozwi±zanie dla podró¿uj±cych w interesach oraz turystów indywidualnych. Stare Miasto i Rynek znajduj± siê w bliskiej odleg³o¶ci od Hotelu. Najstarszy Ogród Botaniczny oraz Obserwatorium Astronomiczne oddalone s± od {{hotel}} zaledwie o 200 metrów .

Wszystkie z 219 nowocze¶nie wyposa¿onych w pe³ni klimatyzowanych pokoi, dysponuje ³azienk±/WC, telefonem, bezprzewodowym internetem WiFi, telewizorem z programami satelitarnymi, a tak¿e radiem.

Profesjonalna obs³uga, rodzinna atmosfera, wysoki standard pokoi oraz zielone otoczenie Hotelu sprawi±, ¿e Pañstwa pobyt w Krakowie stanie siê niezapomnianym prze¿yciem! Hotel po³o¿ony jest blisko centrum miasta i najwa¿niejszych zabytków. Dworzec kolejowy i autobusowy oddalone s± od hotelu tylko parê minut drogi. Kraków to Europejskie miasto kultury i sztuki. Teatr im. Juliusza S³owackiego -miejsce teatralnej awangardy oraz Narodowy Teatr Stary -jedna z najstarszych scen teatralnych w Polsce zlokalizowane s± w niewielkiej odleg³o¶ci od naszego Hotelu. Bie¿±cy Repertuar jest zawsze dostêpny w recepcji."""
    return tpl.replace("{{hotel}}", hotel_name)


def get_conf_desc(conf_name):
    tpl = """Tegoroczne spotkania nosz± podtytu³ "{{konf}}". Pochodz±ce z ³aciny s³owo festivus oznacza: ¿ywy, radosny, weso³y; ¶wi±teczny i dobrze oddaje zarówno dotychczasow± atmosferê Spotkañ, jak i zamierzenia organizatorów wobec tegorocznych. Spotkania bêd± ¿ywym i radosnym (co w ¿adnym wypadku nie oznacza "niepowa¿nym") ¶wiêtem polskiego ¶rodowiska informatycznego.

W strukturze Spotkañ mo¿na wydzieliæ trzy podstawowe nurty: pierwszy dotyczy eGovernment. To zagraniczne s³owo oddaje zrêcznie co¶, co mo¿na nazwaæ "informatyk± obywatelsk±", czyli zastosowaniem informatyki dla dobra obywateli, a co za tym idzie ujmuje problemy architektoniczne, techniczne i legislacyjne, zwi±zane z tym obszarem. Drugi nurt to informatyka stosowana w du¿ych i ¶rednich przedsiêbiorstwach, jej organizacja, cena, warto¶æ, u¿yteczno¶æ i skuteczno¶æ. Adresatami tego nurtu s± mened¿erowie wysokiego i ¶redniego szczebla ze wspominanych firm. Wreszcie trzeci nurt stanowi sesja naukowa, przedstawiaj±ca wyniki prac polskich uczonych na ¶wiatowym poziomie oraz poruszaj±ca problemy transferu technologii i mo¿liwo¶ci zastosowania wyników prac teoretycznych w praktyce."""
    return tpl.replace("{{konf}}", conf_name)

def get_street():
    return streets[(int)(random() * len(streets))]

def get_city():
    return cities[(int)(random() * len(cities))]

def get_address():
    a = Address()
    a.address = get_street()
    a.city = get_city()
    a.zipcode = get_zipcode()
    a.country = countries[(int)(random()*len(countries))]
    a.save()
    return a
