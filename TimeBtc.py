import datetime
import time
import math
from threading import Thread
import BTCcurs as BC
import Sheetsprocess as SP



ost_m=int()
ost_s=int()
ost = str()
d= datetime.datetime.today()

def game_time(d):

    s= d.second
    m = d.minute
    if m % 5 != 0:
        ost_m = 5 - m % 5
    elif m % 5 == 0:
        ost_m = 0
    if s % 60 != 0:
        ost_s = (60 - s % 60) // 1
        if ost_m >= 1:
            ost_m = ost_m - 1
    elif s % 60 == 0:
        ost_s = 0;
    ost = str(''+str(ost_m)+' минут '+str(ost_s)+' секунд')
    return ost
print(game_time(d))

def Game():
    m = d.minute

def vr_igri():

    w = time.time()
    d = datetime.datetime.now()
    a = BC.get_latest_bitcoin_price()
    s = d.second
    m = d.minute
    if m % 5 != 0:
        ost_m = 5 - m % 5
    elif m % 5 == 0:
        ost_m = 0
    if s % 60 != 0:
        ost_s = (60 - s % 60) // 1
        if ost_m >= 1:
            ost_m = ost_m - 1
    elif s % 60 == 0:
        ost_s = 0;
    wait = int(ost_s + ost_m * 60)
    #записать начальный курс в БД4
    wait1 = float(wait + w)+300
    return wait1

def Countdown(id1):

    w = time.time()
    d = datetime.datetime.now()
    a = BC.get_latest_bitcoin_price()
    s = d.second
    m = d.minute
    if m % 5 != 0:
        ost_m = 5 - m % 5
    elif m % 5 == 0:
        ost_m = 5
    if s % 60 != 0:
        ost_s = (60 - s % 60) // 1
        if ost_m >= 1:
            ost_m = ost_m - 1
    elif s % 60 == 0:
        ost_s = 0;
    wait = int(ost_s + ost_m * 60)
    #записать начальный курс в БД4
    wait1 = float(wait + w)
    wait_f = int(wait1//10)
    start = time.strftime("%H:%M:%S", time.localtime(wait1))
    wait2 = wait1+300
    end = time.strftime("%H:%M:%S", time.localtime(wait2))
    SP.Stavka(id1,wait1)
    SP.clear()
    time.sleep(wait)
    sp = BC.get_latest_bitcoin_price()
    sp = round(sp,2)
    nu = SP.kol_uch(wait_f)
    res = SP.nachalo(wait_f, id1)
    vi = res[1] * 2 * sp
    vi = round(vi,2)
    ob = res[0] * sp
    ob = round(ob,2)
    return vi, ob, nu , wait1, wait_f, sp

def countdown2(nu,id1,sp, wait1):
    if nu>1:

        time.sleep(300)
        d2 = int((time.time())//100)
        c = BC.get_latest_bitcoin_price()

        SP.GameTime(d2,c,id1,sp)
        SP.print_res(wait1,id1)
        SP.saveres()
        return True
    else:
        return False









#if ost_s + ost_m = 0






