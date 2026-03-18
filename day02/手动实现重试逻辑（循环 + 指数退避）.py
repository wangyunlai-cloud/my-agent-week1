import random
import time


def perform_task():
    "模拟任务可能抛出的异常"
    if random.random()<0.7:
        raise ValueError("任务失败")
    return "任务成功"

def retry_task(max_retries = 5,base_delay = 1,max_delay =16):
    retrie = 0
    while retrie<max_retries:
        try:
            result = perform_task()
            return result
        except ValueError as e:
            retrie+=1
            delay = min(base_delay*(2**retrie),max_delay)
            print(f"任务失败,第{retrie}次重试...,需要等待{delay}秒")
            time.sleep(delay)
    raise Exception(f"任务重试{max_retries}次后仍然失败")


try:
    result = retry_task()
    print(result)
except Exception as e:
    print(e)



