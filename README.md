# ostoslistaSovellus

## Kuvaus

Ostoslista sovellus tarjoaa käyttäjilleen mahdollisuuden tehdä ryhmiä, joilla on yhteinen ostoslista. Ryhmän tekijä voi lisätä tai poistaa käyttäjiä ryhmästä heidän käyttäjänimen perusteella. Kukin ryhmän jäsen voi lisätä ryhmän ostoslistaan tuotteita.

### Käyttäjätunnus
username: hello

password: world

## Asennusohjeet (Linux)

1. Siirry terminaalissa haluamaasi kansioon cd komennolla
2. Kopioi repositorio komennolla ``git clone https://github.com/tulma95/ostoslistaSovellus.git``
3. Siirry repositorioon komennolla ``cd ostoslistaSovellus``
4. Luo virtual environment komennolla ``python3 -m venv venv``
5. Aktivoi juuri luotu venv komennolla ``source venv/bin/activate``
6. Asenna sovelluksen riippuvuudet komennolla ``pip install -r requirements.txt``
7. Käynnistä sovellus komennolla ``python3 run.py``
8. Mene selaimella osoitteeseen ``localhost:5000``


## Linkkejä
[Sovellus herokussa](https://pro-ostoslista-sovellus.herokuapp.com/)

[Tietokantakaavio](https://github.com/tulma95/ostoslistaSovellus/blob/master/documentation/DatabaseChart.png)

[user storyt](https://github.com/tulma95/ostoslistaSovellus/blob/master/documentation/userStories.md)
