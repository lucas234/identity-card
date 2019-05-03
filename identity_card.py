# _*_ coding=utf-8 _*_
import re
from datetime import datetime, date, timedelta
import random
from regions import regions


class IdentityCardWrongException(Exception):
    pass


class IdentityCard(object):
    def __init__(self, id_card, locale='zh-cn'):
        self.id_card = id_card
        self.locale = locale
        if not self.is_id_card(self.id_card):
            raise IdentityCardWrongException("身份证号码无效!")

    @classmethod
    def is_id_card(cls, id_card):
        if len(id_card) != 18:
            return False  # "Length error"
        if not re.match(r"^\d{17}(\d|X|x)$", id_card):
            return False  # "Format error"
        if id_card[0:6] not in regions:
            return False  # "Area code error"
        if not cls.is_date(id_card):
            return cls.is_date(id_card)
        if str(cls.get_id_card_verify_number(id_card)) != str(id_card.upper()[-1]):
            return False  # "Check code error"
        return True

    @classmethod
    def get_id_card_verify_number(cls, id_card):
        factor = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        check_code_list = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
        check_sum = sum([a * b for a, b in zip(factor, [int(a) for a in id_card[0:-1]])])
        return str(check_code_list[check_sum % 11])

    @classmethod
    def is_date(cls, id_card):
        try:
            date(int(id_card[6:10]), int(id_card[10:12]), int(id_card[12:14]))
            return True
        except ValueError as ve:
            return False  # "Datetime error: {0}".format(ve)

    def get_area(self):
        return self.get_province() + " " + self.get_city() + " " + self.get_county()

    def get_province(self):
        return regions[self.id_card[0:2] + "0000"]

    def get_city(self):
        return regions[self.id_card[0:4] + "00"]

    def get_county(self):
        return regions[self.id_card[0:6]]

    def get_gender(self):
        genders = {'zh-cn': ["女", "男"], 'en': ["Female", "Male"]}
        gender = genders.get(self.locale)
        return gender[0] if int(self.id_card[16:17]) % 2 == 0 else gender[1]

    def get_birthday(self):
        return self.id_card[6:10] + "-" + self.id_card[10:12] + "-" + self.id_card[12:14]

    def get_age(self):
        dates = date(int(self.id_card[6:10]), int(self.id_card[10:12]), int(self.id_card[12:14]))
        age = datetime.now().year - dates.year
        if datetime.now().month < dates.month or (
                        datetime.now().month == dates.month and datetime.now().day < dates.day):
            age -= 1
        return age if age > 0 else 0

    def get_zodiac(self):
        zodiac = {
            'zh-cn': ['牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪', '鼠'],
            'en': ['Cow', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Sheep', 'Monkey', 'Chicken', 'Dog', 'Pig',
                   'Rat']}
        index = abs(int(self.id_card[6:10]) - 1901) % 12
        return zodiac.get(self.locale)[index]

    def get_constellation(self):
        constellations = {'zh-cn': ['魔羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座', '狮子座',
                                    '处女座', '天秤座', '天蝎座', '射手座'],
                          'en': ['Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer',
                                 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius']
                          }
        constellation_edge_days = ((1, 21), (2, 20), (3, 21), (4, 21), (5, 22), (6, 22),
                                   (7, 23), (8, 24), (9, 24), (10, 24), (11, 23), (12, 22))
        month = int(self.id_card[10:12])
        day = int(self.id_card[12:14])
        return constellations.get(self.locale)[len(filter(lambda y: y <= (month, day), constellation_edge_days)) % 12]

    def get_info(self):
        return {
            'area': self.get_age(),
            'province': self.get_province(),
            'city': self.get_city(),
            'county': self.get_county(),
            'gender': self.get_gender(),
            'birthday': self.get_birthday(),
            'zodiac': self.get_zodiac(),
            'age': self.get_age(),
            'constellation': self.get_constellation()
        }

    @classmethod
    def generate_id_card(cls):
        area_code = random.choice(regions.keys())
        age = random.randint(18, 50)
        rd = random.randint(0, 999)
        gender = random.choice([0, 1])
        date_string = str(date(date.today().year - age, 1, 1) + timedelta(days=random.randint(0, 364))).replace("-", "")
        if gender == 0:
            gender_num = rd if rd % 2 == 0 else rd + 1
        else:
            gender_num = rd if rd % 2 == 1 else rd - 1
        result = str(area_code) + date_string + str(gender_num).zfill(3)
        check_num = cls.get_id_card_verify_number(result+"0")
        return result + check_num


