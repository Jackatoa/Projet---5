import mysql.connector


class Sqlfunc:
    """Contain all the MySQL functions"""
    mydb2 = mysql.connector.connect(
        host="localhost",
        user="Jackatoa",
        passwd="MSpassword",
        charset="utf8",
        use_unicode=True
    )

    mycursor2 = mydb2.cursor()
    mycursor2.execute('SET NAMES utf8mb4;')
    mycursor2.execute('SET CHARACTER SET utf8mb4;')
    mycursor2.execute('SET character_set_connection=utf8mb4;')
    mycursor2.execute("create database IF NOT EXISTS food CHARACTER SET utf8mb4 COLLATE "
                      "utf8mb4_unicode_ci;")

    mydb = mysql.connector.connect(
        host="localhost",
        user="Jackatoa",
        passwd="MSpassword",
        database="food",
        use_unicode=True,
        charset="utf8mb4"
    )

    mycursor = mydb.cursor()
    mycursor.execute('SET NAMES utf8mb4;')
    mycursor.execute('SET CHARACTER SET utf8mb4;')
    mycursor.execute('SET character_set_connection=utf8mb4;')
    mycursor.execute("create TABLE IF NOT EXISTS alimentsss ("
                     "nom VARCHAR(255), "
                     "allergen TEXT, "
                     "teneur VARCHAR(255), "
                     "additifs VARCHAR(255), "
                     "packaging VARCHAR(255), "
                     "categorie TEXT, "
                     "score VARCHAR(30), "
                     "imageurl VARCHAR(255), "
                     "shop TEXT, "
                     "url VARCHAR(255) PRIMARY KEY)"
                     "ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"
                     )

    mycursor.execute('SET NAMES utf8mb4;')
    mycursor.execute('SET CHARACTER SET utf8mb4;')
    mycursor.execute('SET character_set_connection=utf8mb4;')
    mycursor.execute("create TABLE IF NOT EXISTS newaliments ("
                     "nom VARCHAR(255), "
                     "url VARCHAR(255),"
                     "newnom VARCHAR(255),"
                     "newurl VARCHAR(255),"
                     "CONSTRAINT fk_nom_url FOREIGN KEY (url) REFERENCES alimentsss(url),"
                     "CONSTRAINT fk_newnom_url FOREIGN KEY (newurl) REFERENCES alimentsss(url))"
                     "ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"
                     )

    def insert_record(self, tablename, nom, allergen, teneur, additifs, packaging,
                      categorie, score, imageurl, shop, url):
        """Insert record for an aliment"""
        sql = "INSERT INTO  " + tablename + " (nom, allergen, teneur, additifs, packaging, " \
                                            "categorie, score, imageurl, shop, url) " \
                                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (nom, allergen, teneur, additifs, packaging, categorie, score, imageurl, shop, url +
               chr(
                   300))
        Sqlfunc.mycursor.execute(sql, val)
        Sqlfunc.mydb.commit()



    def get_number_of_rows(self, tablename):
        """Return number of rows mainly to check if DB is empty"""
        Sqlfunc.mycursor.execute("SELECT * FROM " + tablename)
        Sqlfunc.mycursor.fetchall()
        numberofrows = Sqlfunc.mycursor.rowcount
        return numberofrows

    def get_all_aliments_with_categories(self, choice):
        """Return all aliments for a choosen categorie"""
        Sqlfunc.mycursor.execute("SELECT nom FROM alimentsss WHERE categorie LIKE %s",
                                 ("%" + choice + "%",))
        row = Sqlfunc.mycursor.fetchall()
        return row

    def clean_table(self, tablename):
        """Clean the DB"""
        Sqlfunc.mycursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        Sqlfunc.mycursor.execute("TRUNCATE TABLE " + tablename)
        Sqlfunc.mycursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

    def get_something_from(self, name, something):
        Sqlfunc.mycursor.execute("SELECT " + something + " FROM alimentsss WHERE nom LIKE %s "
                                                         "LIMIT 1",
                                 ("%" + name + "%",))
        result = Sqlfunc.mycursor.fetchone()
        return result

    def get_new_aliment_from_super_query(self, query):
        """Return all result"""
        Sqlfunc.mycursor.execute(query)
        result = Sqlfunc.mycursor.fetchall()
        return result

    def save_new_food(self, oldfood, url, newfood, newurl):
        """Insert food and substitued"""
        sql = "INSERT INTO  newaliments (nom, url, newnom, newurl) VALUES (%s, %s, %s, %s)"
        val = (oldfood, url, newfood, newurl)
        Sqlfunc.mycursor.execute(sql, val)
        Sqlfunc.mydb.commit()
        print("Enregistrement réussi !")

    def get_substitued(self):
        """Return substitued aliments"""
        Sqlfunc.mycursor.execute("SELECT * FROM newaliments")
        result = Sqlfunc.mycursor.fetchall()
        return result
