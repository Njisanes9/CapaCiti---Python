import schedule
import time 
import threading


class DailyDigestSchedular(threading.Thread):
    def __init__(self):
        super().__init__()
        self.__stop_running = threading.Event()

    """
        Schedule a task to repeat at the same time everyday
    """

    def schedule_daily(self, hour, minutes,job):
        schedule.clear() #To clear any exisiting scheduled tasks
        schedule.every().day.at(f'{hour:02d}:{minutes:02d}').do(job)

    """
        Start the scheduler as a background thread.
    """    

    def run(self):
        self.__stop_running.clear()
        while not self.__stop_running.is_set():
            schedule.run_pending()
            time.sleep(1)

    
    """
        Stop the scheduler thread
    """

    def stop(self):
        self.__stop_running.set()


if __name__ == '__main__':

    import dd_Email
    email = dd_Email.DailyDigestEmail()

    scheduler = DailyDigestSchedular()
    scheduler.start()

    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min + 1 # schedule for the next miute
    scheduler.schedule_daily(hour,minute,email.send_email)

    time.sleep(60) # keep program alive long enough to ensure send
    scheduler.stop()




