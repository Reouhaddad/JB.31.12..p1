import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="contact"  # Ajoutez le nom de la base de données
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE contact")
def create_table():
    sql = """CREATE TABLE IF NOT EXISTS `mycontacts` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(15) NULL,
    `email` VARCHAR(25) NULL,
    `phone` INT NULL,
    PRIMARY KEY (`id`));
    """
    mycursor.execute(sql)

create_table()

def add_row():
    sql = """INSERT INTO `mycontacts` (`name`, `email`, `phone`) VALUES ('reou', 'rhaddad95200@gmail.com', '0585030899');"""
    mycursor.execute(sql)
    mydb.commit()


add_row()

def get_data():
    sql = """SELECT `id`, `name`, `email`, `phone` FROM `mycontacts` WHERE name = 'reou';"""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

get_data()
print(mydb)
