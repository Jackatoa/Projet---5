import mysql.connector


class Sqlfunc:
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
                     "allergen VARCHAR(255), "
                     "teneur VARCHAR(255), "
                     "additifs VARCHAR(255), "
                     "packaging VARCHAR(255), "
                     "categorie VARCHAR(255), "
                     "score VARCHAR(255), "
                     "url VARCHAR(255)) "
                     "ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"
                     )

    mycursor.execute('SET NAMES utf8mb4;')
    mycursor.execute('SET CHARACTER SET utf8mb4;')
    mycursor.execute('SET character_set_connection=utf8mb4;')
    mycursor.execute("create TABLE IF NOT EXISTS newaliments ("
                     "nom VARCHAR(255), "
                     "newnom VARCHAR(255)) "
                     "ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"
                     )

    def create_autokey(self, tablename):
        Sqlfunc.mycursor.execute("ALTER TABLE " + tablename + "ADD COLUMN id INT AUTO_INCREMENT "
                                                              "PRIMARY KEY")

    def insert_record(self, tablename, nom, allergen, teneur, additifs, packaging,
                      categorie, score, url):
        sql = "INSERT INTO  " + tablename + " (nom, allergen, teneur, additifs, " \
                                            "packaging, categorie, score, url) VALUES (%s, %s, %s, " \
                                            "%s, %s, %s, %s, %s)"
        val = (nom, allergen, teneur, additifs, packaging, categorie, score, url + chr(300))
        Sqlfunc.mycursor.execute('SET NAMES utf8mb4;')
        Sqlfunc.mycursor.execute('SET CHARACTER SET utf8mb4;')
        Sqlfunc.mycursor.execute('SET character_set_connection=utf8mb4;')
        Sqlfunc.mycursor.execute(sql, val)
        Sqlfunc.mydb.commit()

    def get_record(self):
        Sqlfunc.mycursor.execute("SELECT * FROM testtable1")
        myresult = Sqlfunc.mycursor.fetchall()
        for x in myresult:
            print(x)

    def modify_column_type(self, tablename):
        Sqlfunc.mycursor.execute("ALTER TABLE " + tablename + " MODIFY allergen VARCHAR(1000) ")
        Sqlfunc.mycursor.execute("ALTER TABLE " + tablename + " MODIFY url VARCHAR(1000) ")
        Sqlfunc.mycursor.execute("ALTER TABLE " + tablename + " MODIFY categorie VARCHAR(1000) ")
        Sqlfunc.mycursor.execute("ALTER TABLE " + tablename + " MODIFY packaging VARCHAR(1000) ")

    def get_number_of_rows(self, tablename):
        Sqlfunc.mycursor.execute("SELECT * FROM " + tablename)
        Sqlfunc.mycursor.fetchall()
        numberofrows = Sqlfunc.mycursor.rowcount
        return numberofrows

    def get_all_aliments_with_categories(self, choice):
        Sqlfunc.mycursor.execute("SELECT nom FROM alimentsss WHERE categorie LIKE %s",
                                 ("%" + choice + "%",))
        row = Sqlfunc.mycursor.fetchall()
        return row

    def clean_table(self, tablename):
        Sqlfunc.mycursor.execute("TRUNCATE TABLE " + tablename)

    def get_aliments_with_criteria(self):
        Sqlfunc.mycursor.execute("SELECT nom FROM alimentsss WHERE (CONCAT(Column1, Column2) LIKE "
                                 "'%keyword1%') AND (CONCAT(Column1, Column2) LIKE '%keyword2%')")
        row = Sqlfunc.mycursor.fetchall()
        return row

    def get_packaging(self, food):
        Sqlfunc.mycursor.execute("SELECT packaging FROM alimentsss WHERE nom LIKE %s LIMIT 1",
                                 ("%" + food + "%",))
        packaging = Sqlfunc.mycursor.fetchone()
        return packaging

    def get_number_from(self, name):
        Sqlfunc.mycursor.execute("SELECT url FROM alimentsss WHERE nom LIKE %s LIMIT 1",
                                 ("%" + name + "%",))
        number = Sqlfunc.mycursor.fetchone()
        return number

    def get_additives_from(self, name):
        Sqlfunc.mycursor.execute("SELECT additifs FROM alimentsss WHERE nom LIKE %s LIMIT 1",
                                 ("%" + name + "%",))
        additives = Sqlfunc.mycursor.fetchone()
        return additives

    def get_packaging_from(self, name):
        Sqlfunc.mycursor.execute("SELECT packaging FROM alimentsss WHERE nom LIKE %s LIMIT 1",
                                 ("%" + name + "%",))
        packaging = Sqlfunc.mycursor.fetchone()
        return packaging

    def get_score_from(self, name):
        Sqlfunc.mycursor.execute("SELECT score FROM alimentsss WHERE nom LIKE %s LIMIT 1",
                                 ("%" + name + "%",))
        score = Sqlfunc.mycursor.fetchone()
        return score

    def get_allergen_from(self, name):
        Sqlfunc.mycursor.execute("SELECT allergen FROM alimentsss WHERE nom LIKE %s LIMIT 1",
                                 ("%" + name + "%",))
        allergen = Sqlfunc.mycursor.fetchone()
        return allergen

    def get_new_aliment_from_super_query(self, query):
        Sqlfunc.mycursor.execute(query)
        result = Sqlfunc.mycursor.fetchall()
        return result

    def save_new_food(self, oldfood, newfood):
        sql = "INSERT INTO  newaliments (nom, newnom) VALUES (%s, %s)"
        val = (oldfood, newfood)
        Sqlfunc.mycursor.execute('SET NAMES utf8mb4;')
        Sqlfunc.mycursor.execute('SET CHARACTER SET utf8mb4;')
        Sqlfunc.mycursor.execute('SET character_set_connection=utf8mb4;')
        Sqlfunc.mycursor.execute(sql, val)
        Sqlfunc.mydb.commit()
        print("Enregistrement réussi !")

    def get_substitued(self):
        Sqlfunc.mycursor.execute("SELECT * FROM newaliments")
        result = Sqlfunc.mycursor.fetchall()
        return result

    def testechec(self):
        Sqlfunc.mycursor.execute(
            "SELECT * FROM alimentsss WHERE teneur LIKE '%sugars-in-high%' AND categorie LIKE '%meats%'")
        result = Sqlfunc.mycursor.fetchall()
        return result
