'''
Created on Dec 17, 2016

@author: t.roy
'''
from matplotlib.dates import date2num
from datetime import date, datetime, timedelta
from Utils.fileutils import tail
from time import time

def get_now_epoch():
    # @see https://www.linuxquestions.org/questions/programming-9/python-datetime-to-epoch-4175520007/#post5244109
    return int(time.mktime(datetime.datetime.now().timetuple()))

def datestr2float(myd,fmt='%Y-%m-%d'):
    td = datetime.strptime(myd,fmt)
    return date2num(td)

def generate_dates(start_date, end_date):
    td = timedelta(hours=24)
    # input in string format -> change to datetime format
    year, month, day = (int(x) for x in start_date.split('-'))
    current_date = date(year,month,day)
    year, month, day = (int(x) for x in end_date.split('-'))
    end_date = date(year,month,day)
    dtRange = []
    while current_date <= end_date:
        #print current_date,type(current_date)
        dow = getDayOfWeek(str(current_date))
        if dow>0 and dow<6: # only from monday to friday
            dtRange.append(str(current_date))
        current_date += td
    return dtRange
    
def getDayOfWeek(pdate):
    year, month, day = (int(x) for x in pdate.split('-'))
    return datetime(year,month,day,0,0,0,0).isoweekday()
    #ans = date(year, month, day)
    #print ans.strftime("%A")

def getNextDay(pdate):
    #print pdate,len(pdate)
    if len(pdate) <> 10:
        return pdate;
    pyyyy = int(pdate[:4])
    pmm   = int(pdate[5:7])
    pdd   = int(pdate[8:10])
    try:
        nextday = date(pyyyy,pmm,pdd) + timedelta(days=1)
    except Exception, e:
        return str(e)
    #print nextday
    nextday = str(nextday)
#   nextday = nextday.replace("-","")
    return nextday

def getStartDate(fn):
    t=tail(fn)
    if len(t[0])==0:
        return ''
    else:
        t2=t[0].split(",")
        lastdt=t2[0]
        nextdt=getNextDay(lastdt)
        return nextdt
    
def getToday(fm="%Y%m%d"):
    return datetime.today().strftime(fm)

if __name__ == '__main__':
    pass