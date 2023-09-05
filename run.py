from services.connect_smtp import send_email
from config.config import DATATXT

def get_emails() -> list:
    emails_list = []
    count = 0
    with open(DATATXT, encoding='utf-8') as file:
        for i in range(10):
            email = file.readline().strip('\n')
            send_email(email)
            count += 1
            print(count)
    return emails_list


if __name__ == '__main__':
    get_emails()
