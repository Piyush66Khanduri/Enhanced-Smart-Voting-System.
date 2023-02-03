#import mysql.connector
from mysql.connector import connect
import indian_names
import pyotp
def Vt_Id(Vot_id):
    for i in range(0,100):
        s=(pyotp.random_base32())
        Vot_id.append(s[0::5])
    return Vot_id
def nams(n):
    for i in range(100):
        n.append(indian_names.get_full_name('male'))
    return n
if __name__=='__main__':
    vt=[]
    nm=[]
    lis=[]
    tval=[]
    stat='NO'
    Vt_Id(vt)
    nams(nm)
    u=0
    conn=connect(host='localhost',user='root',password='piyush')
    point=conn.cursor()
    point.execute('use voters')
    command="insert into vot_det(name,voter_Id, status) values(%s,%s,%s)"

    for i,j in zip(nm,vt):
        #print(i,j)
        tup=tuple((i,j,stat))
        #lis.append(tup)
        #lis=list(tuple(tup))
        point.execute('insert into vot_det(name,voter_Id,status) VALUES(%s,%s,%s)',tup)
        point.execute("commit")
        tup=()





        '''try:
            point.execute("insert into vot_det(name,voter_Id, status) values('%s','%s','%s)",tup)
            point.execute("commit")
        except:
            j=(pyotp.random_base32())
            j=j[0::5]
            point.execute("insert into vot_det(name,voter_Id, status) values('i','j','stat')")'''

    '''for i in lis:
        print(i)
        point.executemany(command,i)
    print("Entries done")'''
