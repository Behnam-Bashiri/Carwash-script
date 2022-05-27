month = {}

def createMonthDictDay():
    for i in range(30):
        month[i+1] = [None]

rooshooyi = 15
nezafat = 20
sefrshooyi = 60

def reserve_earliest():
    try:
        firsttime = month.index(None)
    except IndexError:
        pass    


def WorkTimer(hh,mm,i):
    if 9<=hh<=21 and 0<=mm<=59 :
        dayDict = [0,0,hh,mm]
        if i == 'rooshooyi':
            dayDict[0]=hh
            dayDict[1]=mm
            dayDict[3]+=15
            if dayDict[3] > 59 :
                dayDict[2] += dayDict[3]/60
                dayDict[3] = dayDict[3]%60
        elif i == 'rooshooyi':
            dayDict[0]=hh
            dayDict[1]=mm
            dayDict[3]+=20
            if dayDict[3] > 59 :
                dayDict[2] += dayDict[3]/60
                dayDict[3] = dayDict[3]%60
        elif i == 'sefrshooyi':
            dayDict[0]=hh
            dayDict[1]=mm
            dayDict[3]+=60
            if dayDict[3] > 59 :
                dayDict[2] += dayDict[3]/60
                dayDict[3] = dayDict[3]%60
        return dayDict

def reserved(dd,hh,mm,works):
    day = month[dd] 
    if day == None: 
        for i in works:
            day.append(WorkTimer(hh,mm,i))
            print('reserved ({} {}:{})'.format(day,hh,mm))
    else:
        for time in day:
            if time[0] == hh and time[2] == hh:
                if time[3]>mm :
                    print('cannot be reserved')
                else:
                    res = [0,0]
                    for i in works:
                        res[0] += WorkTimer(hh,mm,i)[2]
                        res[1] += WorkTimer(hh,mm,i)[3]
                    reserved(dd,res[2],res[3],[])
            else:
                res = [0,0]
                for i in works:
                    res[0] += WorkTimer(hh,mm,i)[2]
                    res[1] += WorkTimer(hh,mm,i)[3]
                reserved(dd,res[2],res[3],[])
        print('reserved ({} {}:{})'.format(day,hh,mm))

if __name__ == '__main__':
    createMonthDictDay()
    inputUser = str(input("select services : \n reserveEarliest works(+)\n reserve dd hh:mm works(+)\n"))
    typeService=inputUser.split()[0]
    if typeService == 'reserveEarliest' :
        reserve_earliest()
    elif typeService == 'reserve':
        dd = inputUser.split()[1]
        hh = inputUser.split()[2].split(':')[0]
        mm = inputUser.split()[2].split(':')[1]
        works = inputUser.split()[3].split('+')
        reserved(dd,hh,mm,works)