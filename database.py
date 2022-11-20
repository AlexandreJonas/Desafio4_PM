def conectar():
    import sqlite3
    db = sqlite3.connect("desafio.sdb")
    return db

def create_db():
    db = conectar()
    cursor = db.cursor()
    try:
        cursor.execute("CREATE TABLE contato (email , assunto , descricao)")
    except:
        pass
    db.close()

def InsertDB(email, assunto, descricao):
    db = conectar()
    cursor = db.cursor()
    s = f"INSERT INTO contato (email, assunto , descricao ) VALUES ('{email}' , '{assunto}' , '{descricao}')"
    print(s)
    cursor.execute(s)
    db.commit()
    db.close()


def teste():
    db = conectar()
    cursor = db.cursor()
    res = cursor.execute("SELECT * FROM contato")
    sla = res.fetchall()
    db.close()
    return sla
