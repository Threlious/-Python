import re
re_name = re.compile(r'\w+(?=@)')
re_domain = re.compile(r'(?<=@)\w+[.]\w+')


def email_parse(email_address):
    if re_domain.search(email_address) is None:
        raise ValueError
    email_dict = {'name': re_name.search(email_address)[0], 'domain': re_domain.search(email_address)[0]}
    print(email_dict)


email_parse("ma_melnik97@mail.ru")
