```
CREATE TABLE grp (
        id INTEGER NOT NULL,
        name VARCHAR(50) NOT NULL,
        "groupCreator" VARCHAR(50) NOT NULL,
        PRIMARY KEY (id)
)
```
```
CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (username)
)
```
```
CREATE TABLE product (
        id INTEGER NOT NULL,
        name VARCHAR(50) NOT NULL,
        count INTEGER NOT NULL,
        groupid INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(groupid) REFERENCES grp (id)
)
```
```
CREATE TABLE group_users (
        account_id INTEGER,
        group_id INTEGER,
        FOREIGN KEY(account_id) REFERENCES account (id) ON DELETE cascade,
        FOREIGN KEY(group_id) REFERENCES grp (id) ON DELETE cascade
)
```