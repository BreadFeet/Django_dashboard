class WeatherData:
    def chart3(self, loc):
        if loc == 's':
            data = [{'name': 'Seoul',
                     'data': [7.0, 6.9, 9.5, 18.5, 23.4, 28.5, 30.2, 33.5, 29.3, 26.3, 13.9, 9.6]}]
        elif loc == 'b':
            data = [{'name': 'Busan',
                     'data': [5.9, 9.2, 15.7, 18.5, 27.9, 35.2, 36.0, 31.6, 28.2, 18.3, 16.6, 6.8]}]
        elif loc == 'l':
            data = [{'name': 'London',
                     'marker': {'symbol': 'diamond'},
                     'data': [{'y': 3.9,
                              'marker': {'symbol': 'url(https://www.highcharts.com/samples/graphics/snow.png)'}},
                                  4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]}]
        elif loc == 't':
            data = [{'name': 'Tokyo',
                     'marker': {'symbol': 'square'},
                     'data': [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2,
                              {'y': 26.5,
                               'marker': {'symbol': 'url(https://www.highcharts.com/samples/graphics/sun.png)'}},
                              23.3, 18.3, 13.9, 9.6]}]
        print(data)
        return data
