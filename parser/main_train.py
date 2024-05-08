import requests
from bs4 import BeautifulSoup
from datetime import datetime, date
import datetime
import pytz

from parser.headers import headers


def get_data_from_url(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")  # html.parser
    data = soup.find_all('tr', class_="on")
    data2 = soup.find_all('tr', class_="onx")
    data.extend(data2)

    return data


def info_road(index_url: int = 0, all_info: bool = False):
    urls = [
        f'https://swrailway.gov.ua/timetable/eltrain/?geo1=32&geo2=43&eventdate={date.today()}',
        f'https://swrailway.gov.ua/timetable/eltrain/?geo1=43&geo2=32&eventdate={date.today()}'
    ]
    array_for_time = []
    all_array = []

    for i in get_data_from_url(urls[index_url]):
        now = datetime.datetime.now()
        kiev_timezone = pytz.timezone('Europe/Kiev')
        kiev_time = now.astimezone(kiev_timezone)
        try:
            if index_url:
                time = i.find_all("td", class_='tm')[1]
            else:
                time = i.find_all("td")[3].text

            num = i.find("a", class_="et").find("b").text

            road = i.find_all("td")[2].text.strip()

            all_array.append({"num": num, "road": road, "time": time})

            if time >= kiev_time.strftime('%H:%M:%S'):
                array_for_time.append({"num": num, "road": road, "time": time})
        except AttributeError:
            pass

    if all_info:
        # max_road_length = max(len(i.get('road', '')) for i in all_array)
        # for item in all_array:
        #     item['road'] = item.get('road', '').rjust(max_road_length)
        all_array = sorted(all_array, key=lambda x: x['time'])
        return all_array

    # max_road_length = max(len(item.get('road', '').strip()) for item in array_for_time)
    # for item in array_for_time:
    #     item['road'] = item.get('road', '').ljust(max_road_length)
    array_for_time = sorted(array_for_time, key=lambda x: x['time'])
    return array_for_time
