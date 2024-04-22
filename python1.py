import random
import time
import logging

logger = logging.getLogger("logs")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s | %(message)s")
file_handler = logging.FileHandler('trafficlight.txt')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def timer_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        logger.info(f"Время выполнения: {end_time - start_time} секунд")
    return wrapper

@timer_decorator
def trafficlight():
    totaltime = random.randint(30,60)
    logger.info(f"Полное время светофора: {totaltime}")
    timer = random.randint(0, totaltime)
    logger.info(f"Текущее положение таймера: {timer}")
    redtime = totaltime * 2 // 3
    greentime = (totaltime - redtime) * 2 // 3
    while(1):   
        logger.info("Пешеход посмотрел на светофор")
        if (redtime < timer <= redtime + greentime):
            logger.info("Пешеход перешёл дорогу")
            break
        elif (timer <= redtime):
            logger.info(f"Горит красный свет ещё - {timer}")
        else:
            logger.info(f"Горит желтый свет ещё - {timer - redtime - greentime}")
        person = random.randint(4,8)
        timer -= person
        if (timer <= 0):
            timer = totaltime
        time.sleep(person)

def main():
    trafficlight()

if __name__ == "__main__":
    main()