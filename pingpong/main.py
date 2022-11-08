import time, random

from threading import Condition
from concurrent.futures import ThreadPoolExecutor


def task(cond: Condition, text: str, is_first: bool = False, iteration_count: int = 3) -> None:
    if not is_first:
        with cond:
            cond.wait()

    counter = 0

    while 1:
        time.sleep(random.randint(1, 5) * 0.1)
        with cond:
            print(text)
            cond.notify_all()

            if counter >= iteration_count:
                break
            
            counter += 1
            cond.wait()


def main() -> None:
    cond = Condition()
    with ThreadPoolExecutor(3) as executor:
        executor.submit(task, cond, "PING", True)
        executor.submit(task, cond, "PONG")


if __name__ == '__main__':
    main()
