## Käyttötapaukset
|Rooli          | Haluan...                    |Jotta...                                                         | Tilanne  |
|-              |-                             |-                                                                |-        |
|Käyttäjä       |rekisteröidä uuden käyttäjän  |voin liittyä ryhmiin                                             | OK      |
|Käyttäjä       |poistaa käyttäjäni            |voin poistaa poistaa käyttäjäni, kun sille ei ole enää tarvetta  | OK      |
|Käyttäjä       |tehdä uusia ryhmiä            |voin tehdä ostoslistan ryhmälle                                  | OK      |
|Käyttäjä       |lisätä tuotteita ostoslistaan |ryhmän jäsenet tietävät mitä kaupasta tarvitaan         	       | OK      |
|Käyttäjä	      |poistua ryhmästä              |voin lähteä ryhmästä, johon en halua kuulua                      | OK      |
|Ryhmän tekijä  |lisätä käyttäjiä ryhmään      |ryhmässä ei olisi yksinäistä	                                   | OK      |
|Ryhmän tekijä  |poistaa ryhmän                |voin poistaa turhat ryhmät                                       | Kesken  |


## SQL-kyselyt


### Käyttäjän rekisteröinti
```
INSERT INTO account (date_created, date_modified, name, username, password) 
  VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?);
```

### Käyttäjän poisto

Poistetaan käyttäjän tiedot liitostaulusta:
```
DELETE FROM group_users WHERE account_id = ?;
```

Jonka jälkeen poistetaan käyttäjä:
```
DELETE FROM account WHERE account.id = ?;
```

### Ryhmän luominen
```
INSERT INTO grp (name, "groupCreator")
  VALUES (?, ?);
```

### Tuotteen luominen
```
INSERT INTO product (name, count, "groupId") 
  VALUES (?, ?, ?);
```

### Ryhmästä poistuminen
```
DELETE FROM group_users 
  WHERE group_users.account_id = ? AND group_users.group_id = ?;
```

### Käyttäjän lisääminen ryhmään
```
INSERT INTO group_users (account_id, group_id)
  VALUES (?, ?);
```

### Ryhmien listaaminen ja tuotteiden määrän hakeminen
```
SELECT grp.*, (SELECT COUNT(id) FROM Product WHERE Product.groupid = grp.id) AS GroupItemCount
  FROM Grp
  LEFT JOIN Product on Product.id = Grp.id
  JOIN group_users ON Grp.id = group_users.group_Id
  JOIN Account ON Account.id = group_users.account_Id
  WHERE Account.Id = ?
```