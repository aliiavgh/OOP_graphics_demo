from demo import *

def main(): 
    while True: 
        print("""
            Function
        1 - Динамика заболевших по стране (Запрос вводить через точку: 1.0 или 1.1)
                - 0 - мужчины
                - 1 - женщины
        2 - Гендерное соотношение
        3 - Процент выявленных больных по отношению к общему числу пациентов
        4 - Процентное соотношеие всех видов онкологических заболеваний
                - 0 - у мужчин
                - 1 - у женщин

        Выберите область/город: BISHKEK, CITY_OSH, CHUY, NARYN, TALAS, IK(Issy-Kul), JA(Jalal-Abad), OSH, TALAS, BATKEN
                                KR - по стране
        """)
        request = input('Введите запрос(число): ')
        if request == '1.0': 
            men = StatisticsMen(input('Введите область/регион/KR: '), int(input('Введите год (1990-2021): ')))
            return men.graph()
        elif request == '1.1':
            women = StatisticsWomen(input('Введите область/регион/KR: '), int(input('Введите год (1990-2021): ')))
            return women.graph()
        elif request == '2': 
            gen = Gender(input('Введите область/регион/KR: '), int(input('Введите год (1990-2021): ')))
            return gen.gender_per()
        elif request == '3':
            patients = Registered(input('Введите область/регион/KR: '), int(input('Введите год (1990-2021): ')))
            return patients.in_hospital()
        elif request == '4.0': 
            diseases = Diseases(input('Введите область/регион/KR: '), int(input('Введите год (1990-2021): ')))
            return diseases.percent_men()
        elif request == '4.1': 
            diseases = Diseases(input('Введите область/регион/KR: '), int(input('Введите год (1990-2021): ')))
            return diseases.percent_women()

if __name__ == '__main__':
    main()

plt.show()
