import camelot
import re
import pyodbc

def insertData(dsn,nom,nodos,total):
    conn = pyodbc.connect(DSN=dsn,UID="dba",PWD="ii4pr0g1+3k01")
    cursor = conn.cursor()
    cursor.execute("SET TEMPORARY OPTION CONNECTION_AUTHENTICATION='Company=Progitek;Application=Progitek;Signature=000fa55157edb8e14d818eb4fe3db41447146f1571g7cf6b1c162e7a4e4925570fc8104c82ac6d466c6'")

    query = f"INSERT INTO compte_recevoir(nodos,nom,total) VALUES('{nodos}','{nom}','{total}')"
    cursor.execute(query)
    cursor.commit()

    conn.close()

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
      
file = 'C:/ii4net/migCAR/taux_brh/2022-2023.pdf'
tables = camelot.read_pdf(file, flavor='stream', pages="all")
pages = len(tables)
tables[0].df
tables[0].df.shape[0]
for page in range(0, pages):
    lastRowIndex = tables[page].df.shape[0]-1
    lastColIndex = tables[page].df.shape[1]-1
    print(f'-----------DATA FROM PAGE {page}----------')
    date = None
    taux = None

    for i in range(0, lastRowIndex):
        date = None
        taux = None
        if isfloat(tables[page].df.iloc[i,3].replace(",",".").strip()) == True:
            date = tables[page].df.iloc[i,0].replace(",",".").strip()
            taux = tables[page].df.iloc[i,3].replace(",",".").strip()
            print(f'Taux HTG/USD du {date} = {taux}')
        if isfloat(tables[page].df.iloc[i,lastRowIndex].replace(",",".").strip()) == True:
            date = tables[page].df.iloc[i,4].replace(",",".").strip()
            taux = tables[page].df.iloc[i,lastRowIndex].replace(",",".").strip()
            print(f'Taux HTG/USD du {date} = {taux}')

print('---------- OPERATION IS DONE ----------')