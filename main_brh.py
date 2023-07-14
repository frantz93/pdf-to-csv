import camelot
from datetime import datetime
import re
import pandas as pd
import os

monthAbb = ['jan','janv','feb','févr','mar','mars','apr','avr','may','mai','jun','juin','jul','juil','aug','août','sep','sept','oct','nov','dec','déc']
monthNum = ['01','01','02','02','03','03','04','04','05','05','06','06','07','07','08','08','09','09','10','11','12','12']

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def convertBRH(filepath, filename):
    global totalCount
    print(f'Converting data from file : {filename}')
    taux_brh = pd.DataFrame(columns=['DATE', 'TAUX'])

    try: 
        tables = camelot.read_pdf(filepath, flavor='stream', pages="all")
    except: 
        return pd.DataFrame()
    
    pages = len(tables)
    pageRecord = 0
    allRecord = 0

    for page in range(0, pages):
        for i in range(0, tables[page].shape[0]):
            for j in range(0, tables[page].shape[1]):
                val = tables[page].df.iloc[i,j].lower()
                if len(re.findall('\d+-(\D+)-\d+', val)) != 0:
                    month = re.findall('\d+-(\D+)-\d+', val)[0]
                    date = val.replace(month, monthNum[monthAbb.index(month)])
                    #try: date = datetime.strptime(date, '%d-%m-%y').date()
                    #except: pass
                    for k in range(j+1, tables[page].shape[1]):
                        if isfloat(tables[page].df.iloc[i,k].replace(",",".")) == True:
                            rate = str(tables[page].df.iloc[i,k].replace(".",","))
                            #print(f'{date}    {rate}')
                            obs = pd.DataFrame([[date, rate]], columns=['DATE', 'TAUX'])
                            taux_brh = pd.concat([taux_brh, obs], axis=0)
                            pageRecord += 1
                            allRecord += 1
                            totalCount += 1
                            break

        print(f'Page {page+1}/{pages}: {pageRecord} obs')
        pageRecord = 0
    print(f'Total = {allRecord} observations')

    return taux_brh
    #taux_brh = taux_brh.sort_values(by='DATE',ascending=True)


startRep = 'C:\\Users\\user\\Desktop\\github\\pdf-to-csv\\working_files\\'  # Change to the default folderpath with the BRH pdf files
destRep = 'C:\\Users\\user\\Desktop\\github\\pdf-to-csv\\working_files\\' # Change to the default folderpath where you want to save the csv file
filenames = os.listdir(startRep)
totalCount = 0
i = 0

for each in filenames:
    filepath = os.path.join(startRep, each)
    taux_brh = convertBRH(filepath, each)
    if not taux_brh.empty:
        if i > 0:
            taux_brh.to_csv(destRep + 'taux_brh.csv',  mode='a', header=False, index=False, encoding='UTF-8', sep=';')
        else:
            taux_brh.to_csv(destRep + 'taux_brh.csv', index=False, encoding='UTF-8', sep=';')
        i += 1
    else: print(f'Skipped file: {each}. Camelot cannot extract tables.')

print(f'----Operation Finished. {totalCount} lines of data have been converted to csv file----')