import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class OpenStreetMapScraper:
    def __init__(self, headless: bool = True):
        self.options = Options()
        if headless:
            self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)
    
    def __del__(self):
        self.driver.quit()

    def geocode_osm(self, q):
        link = f'https://nominatim.openstreetmap.org/search?format=json&q={q}'
        response = requests.get(link)

        if response.status_code == 200:
            return response.json()

        return [{'osm_id': False}]

    def get_way_osm(self, end):
        q = ''
        for i, palavra in enumerate(end.split(' ')):
            if i < 0 or i + 1 == len(end.split(' ')):
                q += palavra
                break

            q += f'{palavra}_'

        infos = self.geocode_osm(q)

        if len(infos) < 1:
            return False

        if not infos[0]['osm_id']:
            return False

        ways = []
        for arr in infos:
            ways.append(arr['osm_id'])

        return ways

    def get_ponts_links(self, arr):
        pontos_if = []
        for way in arr:
            self.driver.get(f'https://www.openstreetmap.org/way/{way}')
            time.sleep(2)

            xpath_sb = '//*[@id="sidebar_content"]/div[2]'
            sidebar = self.driver.find_element(By.XPATH, xpath_sb)

            details = sidebar.find_elements(By.TAG_NAME, 'details')
            xpath = f'//*[@id="sidebar_content"]/div[2]/details[{len(details)}]/ul'

            ul = self.driver.find_element(By.XPATH, xpath)
            lis = ul.find_elements(By.TAG_NAME, 'li')

            links = []
            for li in lis:
                links.append(li.find_element(By.TAG_NAME, 'a').get_attribute('href'))
            pontos_if.append([links[0], links[-1]])

        return pontos_if

    def get_coordenadas(self, links):
        coordenadas = {}
        for i, link in enumerate(links):
            for j, coord in enumerate(link):
                self.driver.get(f'{coord}')
                time.sleep(2)

                xpath_lat = '//*[@id="sidebar_content"]/div[2]/ul/li[3]/a/span[1]'
                xpath_lng = '//*[@id="sidebar_content"]/div[2]/ul/li[3]/a/span[2]'

                if j == 0:
                    latitude = self.driver.find_element(By.XPATH, xpath_lat).text
                    longitude = self.driver.find_element(By.XPATH, xpath_lng).text
                else:
                    latitude_f = self.driver.find_element(By.XPATH, xpath_lat).text
                    longitude_f = self.driver.find_element(By.XPATH, xpath_lng).text

                    coordenadas[f'trecho{i+1}'] = {
                        'coordIni': {
                            'lat': latitude,
                            'lng': longitude
                        },
                        'coordFim': {
                            'lat': latitude_f,
                            'lng': longitude_f
                        }}

        return coordenadas
