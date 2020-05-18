import re


def validateEmail(email):
    if len(email) > 6:
        if re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', email) != None:
            return 1
    return 0


from django.core.mail import send_mail


def send_parent_invitation(receiver, hash):
    # TODO dorobić wysyólanie z ssl oraz z dedykowanej poczty
    # TODO html template + potwierdzenie otwarcia emaila.
    try:
        send_mail(
            'Link do rejestracji',
            f'Link do rejestrac http://localhost:8000/account/parent/inv/{hash}',
            'from@example.com',
            [receiver],
            fail_silently=False,
        )
        return True
    except Exception as ex:
        return ex


import random


def hash_generator():
    my_hash = random.getrandbits(128)
    return "%032x" % my_hash
