from unittest import result
import psycopg2 as db
import os
con = None
connected = None
cursor = None
def connect():
    global connected
    global con
    global cursor
    try:
        con = db.connect(host="localhost",database="testdb",port=5432,user="sari",password="87654321")
        cursor = con.cursor()
        connected = True
    except :
        connected = False
    return cursor

def disconnect():
    global connected
    global con
    global cursor
    if (connected==True):
        cursor.close()
        con.close()
    else:
        con = None
    connected = False

def Tampil():
    a = connect()
    sql="select * from mahasiswa"
    a.execute(sql)
    results = a.fetchall()

    if a.rowcount < 0:
        print("Tidak ada data mahasiswa.")
    else :
        for data in results:
            print(data)


def Entry():
    global connected
    global con
    global cursor
    xidmhs = input("Masukan ID Mahasiswa: ")
    xnim = input("Masukan NIM: ")
    xnama = input("Masukan Nama Lengkap:")
    xidfk = input("Masukan ID fakultas (1 .. 5): ")
    xidpr = input("Masukan ID prodi (1 .. 10): ")
    a = connect()
    sql = "insert into mahasiswa (idmhs, nim, nama, idfakultastas, idprodi) values ('"+xidmhs+"','"+xnim+"','"+xnama+"','"+xidfk+"','"+xidpr+"')"
    a.execute(sql)
    con.commit()
    print("Entry is done.")

def Cari():
    global connected
    global con
    global cursor
    xnim = input("Masukkan NIM yg dicari: ")
    a = connect()
    sql = "select * from mahasiswa where nim ='" + xnim +"'"
    a.execute(sql)
    record = a.fetchall()
    print(record)
    print("search is done.")

def Ubah():
    global connected
    global con
    global cursor
    xnim = input("Masukkan NIM yg dicari: ")
    a = connect()
    sql = "select * from mahasiswa where nim ='" + xnim + "'"
    a.execute(sql)
    record = a.fetchall()
    print("Data saat ini :")
    print(record)
    row = a.rowcount
    if(row==1):
        print("Silahkan untuk mengubah data..")
        xidmhs = input("Masukan ID Mahasiswa: ")
        xnama = input("Masukkan Nama Lengkap: ")
        xidfk = input("Masukkan ID Fakultas (1 .. 5): ")
        xidpr = input("Masukkan ID Prodi (1 .. 10): ")
        a = connect()
        sql = "update mahasiswa set idmhs='"+ xidmhs +"', nama='" + xnama +"',idfakultastas='"+ xidfk +"', idprodi='" + xidpr + "' where nim='" + xnim + "'"
        a.execute(sql)
        con.commit()
        print("Update is done.")
        sql="select * from mahasiswa where nim='" + xnim + "'"
        a.execute(sql)
        rec = a.fetchall()
        print("Data setelah diubah :")
        print(rec)

    else:
        print("Data tidak ditemukan")

def Hapus():
    global connected
    global con
    global cursor
    xnim = input("Masukkan NIM yg dicari: ")
    a = connect()
    sql = "select * from mahasiswa where nim ='" + xnim + "'"
    a.execute(sql)
    record = a.fetchall()
    print("Data saat ini :")
    print(record)
    row = a.rowcount
    if(row==1):
        jwb=input("Apakah ingin menghapus data? (y/t)")
        if(jwb.upper()=="Y"):
            a = connect()
            sql = "delete from mahasiswa where nim='" + xnim + "'"
            a.execute(sql)
            con.commit()
            print("Delete is done.")
        else:
            print("Data batal untuk dihapus.")
    else:
        print("Data tidak ditemukan")

def show_menu():
    print("=== APLIKASI DATABASE PYTHON ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Keluar")
    print("_ _ _ _ _ _")
    menu = input("pilih menu>")

    #clear screen
    os.system("clear")

    if menu == "1" :
        Tampil()
    elif menu == "2" :
        Entry()
    elif menu == "3" :
        Cari()
    elif menu == "4" :
        Ubah()
    elif menu == "5" :
        Hapus()
    elif menu == "0" :
        exit()
    else:
        print("Menu salah!")

if __name__ == "__main__":
    while(True):
        show_menu()

