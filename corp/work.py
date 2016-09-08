from random import randint

class WorkerStrikeException(Exception):
    pass

class Worker(object):
    """
    A Worker will work a full 40 hour week and then go on strike. Each time
    a Worker works, they work a random amount of time between 1 and 40.
    """
    def __init__(self):
        self.hours_worked = 0

    def work(self):
        timesheet = randint(1, 40)
        self.hours_worked += timesheet
        if self.hours_worked > 40:
            raise WorkerStrikeException("This worker is picketing")

        return timesheet

class Boss(object):
    """
    A Boss makes profit using workers. Bosses squeeze 1000 monies out of a
    Worker for each hour worked. Workers on strike are instantly replaced.
    """
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
