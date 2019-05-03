# ostoslistaSovellus

## Kuvaus

Ostoslista sovellus tarjoaa käyttäjilleen mahdollisuuden tehdä ryhmiä, joilla on yhteinen ostoslista. Ryhmän tekijä voi lisätä tai poistaa käyttäjiä ryhmästä heidän käyttäjänimen perusteella. Kukin ryhmän jäsen voi lisätä ryhmän ostoslistaan tuotteita.

### Käyttäjätunnus
username: hello

password: world

## Linkkejä
[Sovellus herokussa](https://pro-ostoslista-sovellus.herokuapp.com/)

[Tietokantakaavio](https://github.com/tulma95/ostoslistaSovellus/blob/master/documentation/DatabaseChart.png)

[user storyt](https://github.com/tulma95/ostoslistaSovellus/blob/master/documentation/userStories.md)

## Asennusohjeet (Linux)

1. Siirry terminaalissa haluamaasi kansioon cd komennolla
2. Kopioi repositorio komennolla ``git clone https://github.com/tulma95/ostoslistaSovellus.git``
3. Siirry repositorioon komennolla ``cd ostoslistaSovellus``
4. Luo virtual environment komennolla ``python3 -m venv venv``
5. Aktivoi juuri luotu venv komennolla ``source venv/bin/activate``
6. Asenna sovelluksen riippuvuudet komennolla ``pip install -r requirements.txt``
7. Käynnistä sovellus komennolla ``python3 run.py``
8. Mene selaimella osoitteeseen ``localhost:5000``

## Asennusohjeet (Heroku)

1. Luo uusi heroku sovellus komennolla ``heroku create *nimi*``
2. Lisää Herokun tiedot Git-versionhallintaan ``git remote add heroku https://git.heroku.com/*sovelluksenNimi*.git``
3. Tee ensimmäinen committi ja puske se herokuun 
```
git add .
git commit -m "Initial commit"
git push heroku master
```
4. Lisää herokuun tarvittavat asetukset, jotta tietokannan saa toimimaan
```
heroku config:set HEROKU=1
heroku addons:add heroku-postgresql:hobby-dev
```
5. Uudelleenkäynnistä heroku komennolla ``heroku restart``


## Käyttöohjeet

### Sisäänkirjautumaton käyttäjä

#### Aloitusnäkymä ####
Sovelluksen alkunäkymässä käyttäjä voi valita vasemmassa reunassa olevasta valikosta joko kirjautua sisään tai rekisteröitä uuden käyttäjän.

#### Rekisteröitysmisnäkymä ####
Rekisteröidäkseen uuden käyttäjän, pitää uudelle käyttäjälle antaa nimi, käyttäjätunnus sekä salasana. Käyttäjätunnuksen sekä salasanan täytyy olla 4-12 merkkiä pitkiä ja käyttäjätunnuksen pitää olla uniikki.

#### Kirjautumisnäkymä ####
Kirjautuakseen sisään käyttäjän pitää syöttää hänen käyttäjätilinsä käyttäjätunnus sekä salasana ja painaa Login-nappia.

### Sisäänkirjautunut käyttäjä

#### Aloitusnäkymä #### 
Käyttäjän kirjautuessa sisään, vasemmalla olevaan valikkoon tulee kolme eri vaihtoehtoa jotka ovat "My account", "My groups" ja "Logout".

#### My account-näkymä ####
My account-näkymässä käyttäjä voi tarkastella käyttäjätilinsä tietoja tai poistaa käyttäjätilin Delete account-napilla.

#### My groups-näkymä ####
My groups-näkymässä käyttäjälle näytetään lista ryhmistä joihin hänen käyttäjätili on liitetty. Käyttäjä voi myös halutessaan lisätä uuden ryhmän kirjoittamalla esillä olevaan tekstikenttään uuden ryhmän nimen ja painamalla Add new group-nappia. Klikkaamalla ryhmän nimeä, näkymä siirtyy klikatun ryhmän ostoslistaan.

#### Ostoslistanäkymä ####
Ostoslistanäkymässä yläreunassa lukee valitun ryhmän nimi ja sen alapuolella on info-nappula jota painamalla näkee ryhmästä lisää tietoa. Info-nappulan alapuolella on lista ryhmään lisätyistä tuotteista ja niiden lukumäärää voidaan joko kasvattaa, vähentää tai poistaa tuotteen nimen perässä olevien nappien avulla. Uuden tuotteen lisääminen onnistuu kirjoittamalla tekstikenttään uuden tuotteen nimi ja painamalla Add product-nappia.

#### Ryhmän info-näkymä ####
Ryhmän info-näkymässä käyttäjä voi tarkastella kyseisen ryhmän käyttäjiä ja ryhmän tekijä voi myös lisätä ryhmään käyttäjiä valitsemalla listasta käyttäjän ja painamalla "Add user to group"-nappia. Jos lista on tyhjä, tarkoittaa se sitä, että kaikki mahdolliset käyttäjät ovat jo ryhmässä. Käyttäjä voi myös poistua ryhmästä painamalla "Leave group"-nappia.

#### Logout ####
Logout-nappia painamalla kirjautunut käyttäjä kirjautuu ulos.

