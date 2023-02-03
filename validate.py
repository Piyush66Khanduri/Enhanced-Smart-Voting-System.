from mysql.connector import connect
import main
def find_Det(enu1,enu2,tk):
    print("In validation")
    print(enu1.get(),enu2.get())
    name,vtid=enu1.get(),enu2.get()
    que = f"select status from vot_Det where voter_Id='{vtid}'"
    conn=connect(host='localhost',user='root',password='piyush',database='voters')
    point=conn.cursor()
    try:
        point.execute(que)
    except:
        pass
    j=""
    for i in point:
        for j in i:
            print(j)
    if j=='NO':
        main.ent_mail(tk)
    elif j=='YES':
        main.done(tk)
    else:
        main.none(tk)