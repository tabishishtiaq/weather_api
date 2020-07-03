import requests
import json




def weather_input(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=c73e48a7ec5a89f57f52c48a792e7064&units=metric'.format(
        city)

    result = requests.get(url)
    json_response = json.loads(result.text)






    name = json_response['name'], json_response['sys']['country']
    temp = json_response['main']['temp'], json_response['main']['humidity']
    wind = json_response['wind']['speed']
    location = json_response['coord']['lon'], json_response['coord']['lat']
    description = json_response['weather'][0]['description']

    print('\nYour City and Country name : ' + str(name), '\nYour City Temperature and Humidity : ' + str(temp),
          '\nYour City Wind Speed : ' + str(wind), '\nYour city Location at longitude and latitude : ' + str(location),
          '\nYour City Weather Details : ' + str(description))


city = input('Enter Your City: ')
weather_input(city)




def test_weather_api(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=c73e48a7ec5a89f57f52c48a792e7064&units=metric'.format(
        city)

    try:
        response = requests.get(url)

        if response.status_code == 200:
            assert response.status_code == 200
            print("Weather Api assertion is Passed")
        else:
            print("Weather Api assertion is Failed")

    except Exception as e:
        print("Weather Api assertion is failed Due To : " + str(e))


city = input('Enter Your City: ')
test_weather_api(city)

