import time

from random import randint
from services.connect_smtp import send_email
from config.config import DATATXT

def get_emails() -> list:
    emails_list = []
    count = 0
    with open(DATATXT, encoding='utf-8') as file:
        for i in range(100):
            email = file.readline().strip('\n')
            send_email(email)
            count += 1
            print(count)
            time.sleep(randint(0, 5))
    return emails_list


if __name__ == '__main__':
    get_emails()
