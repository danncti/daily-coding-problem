from threading import Timer
import sys
def task(n):
    print("task completed after %s ms"%(n))

def scheduler(f, n):
    timer = Timer(n/1000, f ,[n])
    timer.start()

def main():

    print("start")
    scheduler(task, 100)
    scheduler(task, 500)
    scheduler(task, 200)
    print("waiting for sheduler tasks")

if __name__ == "__main__":
    main()
