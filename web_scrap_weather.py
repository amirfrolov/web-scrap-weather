from bs4 import BeautifulSoup
import requests

def main():
    #set the url
    url = "https://weather.com/"
    print(f"Scraping {url}")
    try:
        html_text = requests.get(url, auth=('user', 'pass')).text
    except requests.exceptions.ConnectionError:
        print("No enternet connection")
        return None
    #set the scraper
    soup = BeautifulSoup(html_text, features="lxml")
    weather_deg = soup.find(class_="CurrentConditions--tempValue--3KcTQ").text
    print("the weather now is: %s" % weather_deg)
    #print the weather for the next hours
    hourly_weather = soup.find(class_="HourlyWeatherCard--TableWrapper--2kboH").find_all('li')[1:]
    for i in hourly_weather:
        time = i.find("h3").text
        deg = i.find("div").text
        print(time, deg)

    return None
    
if __name__ == "__main__":
    main()
