import oauth2client
import gspread

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import time
import BTCcurs as BT
import TimeBtc as TB







scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('cred1.json', scope)

gc = gspread.authorize(credentials)

sh = gc.open("Humsterobot")


def Get_Token():
    wks = sh.worksheet('id')
    val = wks.cell(1, 5).value
    return val;

def UserList(id1,nm):
    wks = sh.worksheet('id')

    values_list = wks.col_values(1, value_render_option='UNFORMATTED_VALUE')
    if id1 in values_list:
        return True

    elif id1 not in values_list:
        val = len(wks.col_values(1))
        val = int(val)+1

        wks.update_cell(val, 1, id1);
        wks.update_cell(val, 2, nm);
        return False;

def Stavka(course, Btsum, id1,wait1):
    wks = sh.worksheet('id')
    values_list = wks.col_values(1, value_render_option='UNFORMATTED_VALUE')
    if id1 in values_list:

        cell = wks.find(str(id1))
        a = cell.row

        today = time.strftime("%H:%M:%S", time.localtime(wait1))
        endt = time.strftime("%H:%M:%S", time.localtime(wait1+300))
        w = int(wait1//10)
        wks.update_cell(a,9,str(w))
        wks.update_cell(a,4,Btsum)
        wks.update_cell(a,5,course)
        wks.update_cell(a, 6, today)
        wks.update_cell(a,7,endt)

def CheckBalance(id1):
    wks = sh.worksheet('id')
    cell = wks.find(str(id1))
    a= cell.row
    bal =wks.cell(a,3,value_render_option='UNFORMATTED_VALUE').value
    return bal


def GameTime(d2,c,id1,sp):
    wks = sh.worksheet('id')

    values_list = wks.col_values(1, value_render_option='UNFORMATTED_VALUE')
    if id1 in values_list:

        cell = wks.find(str(id1))
        a = cell.row

        wks.update_cell(a, 10, sp)
        wks.update_cell(a, 8, c)
        #Results(d2,c)

def Results(d2,c):
    wks = sh.worksheet('id')
    d3 = int(d2)
    update_cell(16,25,d3)
    print(d3)
    res = wks.findall(str(d3))
    i = 0
    x = len(res)
    while i < x:
        wks = sh.worksheet('id')
        row = res[i].row
        values_list1 = wks.row_values(row, value_render_option='UNFORMATTED_VALUE')
        wks1 = sh.worksheet('game')
        r = len(wks1.col_values(14)) +1
        wks1.update_cell(r, 13, values_list1[0])
        wks1.update_cell(r, 14, values_list1[6])
        wks1.update_cell(r, 15, values_list1[4])
        wks1.update_cell(r, 16, values_list1[3])
        i = i + 1

def Result_2(d2,c) :
    wks1 = sh.worksheet('game')
    n = d2 * 100
    d = time.strftime("%H:%M:%S", time.localtime(n))
    d1 = time.strftime("%d.%m.%Y", time.localtime(n))
    a = len(wks1.col_values(7))
    wks1.update_cell(a, 7, d1)
    wks1.update_cell(a, 8, d)
    wks1.update_cell(a, 9, c)

def update_cell(a,b,c):
    wks = sh.worksheet('game')
    return wks.update_cell(a,b,c)
def get_value(a,b,c):
    wks = sh.worksheet('id')
def id_cell(a,b,c):
    wks= sh.worksheet('id')
    return wks.update_cell(a,b,c)

def clear():
    wks = sh.worksheet('game')
    cell_list = wks.range('G16:I100')

    for cell in cell_list:
        cell.value = ""

    # Update in batch
    wks.update_cells(cell_list)

    cell_list1 = wks.range('M16:P100')

    for cell in cell_list1:
        cell.value = ""

    # Update in batch
    wks.update_cells(cell_list1)

    cell_list2 = wks.range('Y16:AC100')

    for cell in cell_list2:
        cell.value = ""

    # Update in batch
    wks.update_cells(cell_list2)

def print_res(wait1):
    wks = sh.worksheet('id')
    w = int(wait1//10)
    cell = wks.findall(str(w))
    a = int(len(cell))
    i = 0
    while i < len(cell):
        wks = sh.worksheet('id')
        row = cell[i].row
        value = wks.row_values(row)
        add_date(value)
        i = i + 1


def add_date(value):
    wks1 = sh.worksheet('game')
    spisok = wks1.col_values(13,value_render_option="UNFORMATTED_VALUE")

    n0 = value[0]
    n3 = value[3]
    n4 = value[4]
    n5 = value[5]
    n6 = value[6]
    n7 = value[7]
    n8 = value[8]
    n9 = value[9]
    if n0 not in spisok:

        wks1 = sh.worksheet('game')

        ln1 = len(wks1.col_values(13)) + 1
        wks1.update_cell(16, 9, n7)
        wks1.update_cell(ln1, 13, n0)
        wks1.update_cell(ln1, 14, n8)
        wks1.update_cell(ln1, 15, n4)
        wks1.update_cell(ln1, 16, n3)

        wks1.update_cell(16, 8, n6)
        # wks1.update_cell(ln,7,time.strftime("%d:%y:%m", time.time()))

        wks1.update_cell(16, 25, n8)
        wks1.update_cell(16, 26, n9)
        wks1.update_cell(16, 27, n7)
        wks1.update_cell(16, 28, n5)
        wks1.update_cell(16, 29, n6)
    elif n0 in spisok:
        print(1)


def final(id1):
    wks = sh.worksheet('game')
    val = wks.col_values(13, value_render_option='UNFORMATTED_VALUE')
    cel = wks.find(str(id1))
    row = cel.row
    val = wks.row_values(row, value_render_option='UNFORMATTED_VALUE')
    stavka = val[15]
    result = val[22]
    prognoz = val[14]
    result_s = round(val[21], 2)
    result_btc = stavka * result
    result = round(result, 5)
    print(stavka, result, result_s, result_btc)
    curs = wks.acell('I16').value
    if result <= 0:
        text = str('Курс ' + str(curs) + '\n Ваш прогноз ' + str(prognoz) + ' оказался не точным.\n Вы теряете ' + str(
                    result_btc) + 'BTC ' + str(result_s) + '$ ')
    else:
        text = str( 'Курс ' + str(curs) + '\n Ваш прогноз ' + str(prognoz) + ' оказался верным.\n Вы выигрываете ' + str(
                    result_btc) + 'BTC ' + str(result_s) + '$ ')
    balance_fin(result_btc, id1)
    return text

def balance_fin(result_btc, id1):
    wks = sh.worksheet('id')
    cel = wks.findall(str(id1))
    row = cel[0].row
    bal = wks.cell(row, 3, value_render_option="UNFORMATTED_VALUE").value
    nb = float(bal) + float(result_btc)
    wks.update_cell(row, 3, float(nb))

def saveres():
    wks = sh.worksheet('game')
    val = wks.row_values(16, value_render_option="UNFORMATTED_VALUE")
    res = val[24:39]
    saver(res)

def saver(res):
    wks1 = sh.worksheet('game result')
    x = 0
    row = len(wks1.col_values(1)) + 1
    for i in res:
        x = x + 1
        wks1.update_cell(row, x, i)

def kol_uch(wait_f):
    wks = sh.worksheet('id')
    val = wks.col_values(9,value_render_option="UNFORMATTED_VALUE" )
    nu = 0
    for i in val:
        if i == wait_f:
            nu = nu +1
    return nu








    #wks = sh.worksheet('game')



       # wks1= sh.worksheet('game')









#def CheckStavka(Btsum, course):


