import time

class DeltaClock:
    def __init__(self, time_obj1, time_obj2):
        self.time_obj1 = time_obj1
        self.time_obj2 = time_obj2

    def __str__(self):
        #return time.strftime("%H: %M: %S", time.gmtime(self.__len__()))

        time = self.__len__()
        if time > 0:
            hours = time // 3600
            minutes = (time - (hours * 3600)) // 60
            second = time - (hours * 3600) - (minutes * 60)
            time_l = [str(hours), str(minutes), str(second)]
            for i in range(3):
                if len(time_l[i]) == 1:
                    time_l[i] = f'0{time_l[i]}'
            return ': '.join(time_l)
        else:
            return "00: 00: 00"

    def __len__(self):
        return self.time_obj1.get_time() - self.time_obj2.get_time()





class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds





dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)
len_dt = len(dt) # 5400
print(len_dt)