class Data:
    days_in_month = {1:31, 2:28, 3:31, 4:30, 5:30, 6:31, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    dmy_as_str = ''

    def __init__(self, s):
        Data.dmy_as_str = s

    @classmethod
    def dmy_to_int(cls):
        """ Возвращает количество часов """
        s = list(map(int, cls.dmy_as_str.split('-')))
        return s[0]*24 + cls.days_in_month.get(s[1])*24+sum(cls.days_in_month.values())*s[2]*24

    @staticmethod
    def dmy_check():
        dmy = list(map(int, Data.dmy_as_str.split('-')))
        return True if (dmy[0] > 0 or dmy[0] <= Data.days_in_month.get(dmy[1])) and dmy[1] in Data.days_in_month.keys()\
                       and dmy[2] > 0 else False



s = Data('1-12-2023')
print(Data.dmy_check())
print(s.dmy_to_int())
