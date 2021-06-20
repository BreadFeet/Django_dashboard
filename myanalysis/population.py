import csv
import numpy as np

from config.settings import DATA_DIRS


class Population:
    # 서울시 5세이하 영유아 현황
    def age5(self):
        with open(DATA_DIRS[0] + '/age3.csv') as f:
            data = csv.reader(f)
            next(data)
            data = list(data)  # object -> list로 바꿔서 데이터 로딩이 여러번 가능하게 함

            result = []
            for row in data:
                arr = np.array(row[3:9], dtype=int)  # 숫자로 한번에 바꾸기 위해서
                s = int(np.sum(arr))  # numpy.int3 -> int: 사전 만드는 건 문제 없으나, json으로 덤핑 안됨

                # 빈 사전에 name, y 항목을 만들고, list에 append
                d = dict()
                d['name'] = row[0][6: row[0].find('(')]  # 구이름 부분만 뽑아냄
                d['y'] = s
                result.append(d)

        return result

    # 서울시 각 구에서 지난 3년간 인구변화----------------------------------------------------
    def diff3(self):
        with open(DATA_DIRS[0] + '/age4.csv') as f:
            data = csv.reader(f)
            next(data)
            data = list(data)

            diff = []
            name = []
            for row in data:
                diff.append(int(row[27]) - int(row[1]))
                nm = row[0].split(' ')[1]         # 이름 자르는 또다른 방법(강사님)
                name.append(nm)     # 이후 xAxis 부분 채우기 위해서 context로 보낼 수 있을까? -> diff5 확인!!!

            result = [{
                'loc': name
            }, [{
                'name': 'difference between 2018 and 2020',
                'data': diff
            }]]

        return result

    # Day20_num_pan의 함수 복사해옴---------------------------------------------------------------
    def P248(self, loc):
        global diff
        f = open(DATA_DIRS[0] + '/age2.csv')
        data = csv.reader(f)
        next(data)
        data = list(data)

        # 특정 지역의 연령별 비율
        for row in data:
            if loc in row[0]:
                n1 = np.array(row[3:], dtype=int)  # print(n1) 보면 숫자가 string에 담겨 있으므로 dtype 지정
                d1 = int(row[1].replace(',', ''))  # 나누는 수도 콤마 없애고 int로 만들어야 함
                lst1 = (n1 / d1).tolist()
        # print(lst1)

        # # 간단하게 plot 확인하기
        # plt.plot(lst1)
        # plt.show()

        # 비교할 모든 지역의 연령별 비율
        min = 10
        name = ''
        rate = None

        for row in data:
            l = row[3:]  # 일부 콤마있는 값이 있어서 for loop으로 콤마 제거해야! (엑셀서 바꾸고 와도 됨)
            for i in range(len(row[3:])):
                l[i] = l[i].replace(',', '')
            n2 = np.array(l, dtype=int)
            d2 = int(row[1].replace(',', ''))
            # 비율이 가장 비슷한 동네를 어떻게 찾을까? -> array끼리 뺀 차가 가장 작아야 한다
            # 차가 작다는 것은 어떻게 비교하나? -> 차의 합이 가장 작은 지역을 찾으면 됨!
            diff = np.abs((n1 / d1) - (n2 / d2))  # 절대값 붙이지 않으면 가장 동떨어진게 합이 음수라서 최소값이 되어버린다!
            s = np.sum(diff)
            if loc not in row[0] and s <= min:  # 차이가 가장 작은 것은 자기 자신이므로 제외해야 함!
                min = s
                name = row[0]  # 최소값 넣을 때, 그 지역도 바꿔줌
                rate = n2 / d2  # 최소값 넣을 때, 인구 비율도 바꿔줌

        result = [{
            'name': loc,
            'data': lst1
        }, {
            'name': name.split(' ')[1],
            'data': (n2 / d2).tolist()
        }]

        return result

    # 서울시 각 구의 지난 5년간 인구 변화 -  diff3과는 다르게 파일 두개 열어서 비교하도록 함!
    def diff5(self):
        with open(DATA_DIRS[0] + '/age4.csv') as f1:  # 2018~2020 데이터 있는 파일
            data1 = csv.reader(f1)
            next(data1)
            data1 = list(data1)

            f2 = open(DATA_DIRS[0] + '/age5.csv')  # 2015년 데이터만 있는 파일
            data2 = csv.reader(f2)
            next(data2)
            data2 = list(data2)

            name = []
            diff = []
            # for row in data1:
            #     n20 = int(row[27])
            #     nm = row[0].split(' ')[1]
            #     name.append(nm)
            #     for d in data2:
            #         if nm in d[0]:               # 모든 for loop을 다 돌면 안됨! 2015 파일에서 해당 구역만 찾아야함!
            #             n15 = int(d[1])
            #             diff.append(n20 - n15)

            # 강사님 방법 - for loop을 돌려서 두 파일에서 같은 i값을 쓴다
            for i in range(0, len(data1)):
                diff.append(int(data1[i][27]) - int(data2[i][1]))
                nm = data1[i][0].split(' ')[1]
                name.append(nm)

            result = [{
                'loc': name
            }, [{
                'name': 'Population Difference between 2015 and 2020',
                'data': diff
            }]
            ]

            return result


if __name__ == '__main__':
    # Population().age5()
    # Population().diff3()
    # Population().P248('신도림')
    Population().diff5()

# import numpy as np
# n = np.array([1, 2, 3])
# s = np.sum(n)
# print(s, type(s))
#
# lst = []
# d = dict()
# d['숫자'] = s
# lst.append(d)
# print(lst)     # 사전 만드는데는 문제 없음
