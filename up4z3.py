import datetime
import psutil
import sqlite3

con = sqlite3.connect("monitor.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS monitor
            (monitor_time TEXT PRIMARY KEY,
            cpu REAL,
            ram REAL,
            disk REAL)
            """)

while True:
    comm = input("1 monitor now\n2 old monitors\n- stop\n")
    if comm == "1":
        monitor_time = str(datetime.datetime.now())
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()[4]
        disk = psutil.disk_usage("/")[3]
        print(f"time {monitor_time}\ncpu used {cpu}\nram free {ram}\ndisk {disk}")
        cursor.execute('''
                    INSERT INTO monitor (monitor_time, cpu, ram, disk)
                    VALUES (?, ?, ?, ?)
                ''', (monitor_time, cpu, ram, disk))
        con.commit()

    elif comm == "2":
        cursor.execute('SELECT * FROM monitor')
        for i in cursor.fetchall():
            print(i)

    else:
        break
