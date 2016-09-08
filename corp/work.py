from random import randint

class WorkerStrikeException(Exception):
    pass

class Worker(object):
    def __init__(self):
        self.hours_worked = 0

    def work(self):
        timesheet = randint(1, 40)
        self.hours_worked += timesheet
        if self.hours_worked > 40:
            raise WorkerStrikeException("This worker is picketing")

        return timesheet

class Boss(object):
    def __init__(self, worker):
        self.worker = worker
        self.profit = 0

    def make_profit(self):
        try:
            self.profit += self.worker.work()*1000
        except WorkerStrikeException as e:
            print("%s" % e)
            self.worker = Worker()
            self.profit += self.worker.work()*1000
        finally:
            return self.profit

if __name__ == '__main__':
    boss = Boss(Worker())
    print(boss.make_profit())
    print(boss.make_profit())
    print(boss.make_profit())
