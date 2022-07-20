from . import jalali
from django.utils import timezone
import os
from ippanel import Client

def Persian_numbers_converter(mystr):
    numbers = {
        "0":"۰",
        "1":"۱",
        "2":"۲",
        "3":"۳",
        "4":"۴",
        "5":"۵",
        "6":"۶",
        "7":"۷",
        "8":"۸",
        "9":"۹",
    }

    for e, p in numbers.items():
        mystr = mystr.replace(e, p)

    return mystr





def jalali_converter(time):
    jmonths = [
        "فروردین",
        "اردیبهشت",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن",
        "اسفند",
    ]

    time = timezone.localtime(time)

    time_to_str="{},{},{}".format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(time_to_tuple)

    for index, month in enumerate(jmonths):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break

    output = "{} {} {}, ساعت {}:{}".format(
        time_to_list[2],
        time_to_list[1],
        time_to_list[0],
        time.hour,
        time.minute,
    )
    return Persian_numbers_converter(output)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def jalali_converter2(time):
    jmonths = [
        "فروردین",
        "اردیبهشت",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن",
        "اسفند",
    ]

    time = timezone.localdate(time)

    time_to_str="{},{},{}".format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(time_to_tuple)

    for index, month in enumerate(jmonths):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break

    output = "{} {} {}".format(
        time_to_list[2],
        time_to_list[1],
        time_to_list[0],
    )
    return Persian_numbers_converter(output)


def gregorian_converter(time):
    time_to_list = time.split('/')
    time_to_str="{},{},{}".format(time_to_list[0], time_to_list[1], time_to_list[2])
    return(jalali.Persian(time_to_str).gregorian_string())


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def send_otp(user_code, phone_number):
    api_key = "aBqsW_avX_AlBFvTMKWzAOj53Z1F4Lm97WDhbAQnXos="
    sms = Client(api_key)
    credit = sms.get_credit()
    phone_number = "+98" + phone_number[1:]
    # ---- send sms -----
    pattern_values = {
        "code": user_code,
    }
    bulk_id = sms.send_pattern(
        'poyavylj70hwvkx',    # pattern code
        "+98100020400",      # originator
        phone_number,  # recipient
        pattern_values,  # pattern values
    )
    message = sms.get_message(bulk_id)
    # print(message)
    # print(message.status)  # get message status
    # print(message.cost)    # get message cost
    # ---- send sms -----



def send_wellcome_sms(phone_number, name):
    api_key = "aBqsW_avX_AlBFvTMKWzAOj53Z1F4Lm97WDhbAQnXos="
    sms = Client(api_key)
    credit = sms.get_credit()
    phone_number = "+98" + phone_number[1:]
    # print(phone_number)
    # print(name)
    # name = "2222"
    # ---- send sms -----
    pattern_values = {
        "name": name,
    }
    bulk_id = sms.send_pattern(
        '3tilxhzkonrfeg3',    # pattern code
        "+98100020400",      # originator
        phone_number,  # recipient
        pattern_values,  # pattern values
    )
    # message = sms.get_message(bulk_id)
    # print(message)
    # print(message.status)  # get message status
    # print(message.cost)    # get message cost
    # ---- send sms -----


def send_request_resanehdar_sms(phone_number, name):
    api_key = "aBqsW_avX_AlBFvTMKWzAOj53Z1F4Lm97WDhbAQnXos="
    sms = Client(api_key)
    credit = sms.get_credit()
    phone_number = "+98" + phone_number[1:]
    # ---- send sms -----
    pattern_values = {
        "name": name,
    }
    bulk_id = sms.send_pattern(
        'mut5ncxlumwv4t3',    # pattern code
        "+98100020400",      # originator
        phone_number,  # recipient
        pattern_values,  # pattern values
    )
    message = sms.get_message(bulk_id)
    # print(message)
    # print(message.status)  # get message status
    # print(message.cost)    # get message cost
    # ---- send sms -----


def send_verify_resanehdar_sms(phone_number, name):
    api_key = "aBqsW_avX_AlBFvTMKWzAOj53Z1F4Lm97WDhbAQnXos="
    sms = Client(api_key)
    credit = sms.get_credit()
    phone_number = "+98" + phone_number[1:]
    # ---- send sms -----
    pattern_values = {
        "name": name,
    }
    bulk_id = sms.send_pattern(
        '1sg8w5uw6wcgzic',    # pattern code
        "+98100020400",      # originator
        phone_number,  # recipient
        pattern_values,  # pattern values
    )
    message = sms.get_message(bulk_id)
    # print(message)
    # print(message.status)  # get message status
    # print(message.cost)    # get message cost
    # ---- send sms -----
