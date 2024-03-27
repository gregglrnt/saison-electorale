from prisma.models import Meteo

def get_weather_status(meteo: Meteo):
    status = ""
    try:
        if(isinstance(meteo.wind_speed, float)):
            if(meteo.wind_speed > 40.0):
                status += "windy "
        if(isinstance(meteo.rain, float)):
            if(meteo.rain > 2):
                status += "rain "
        if(isinstance(meteo.ice_height, float)):
            if(meteo.ice_height > 0.025):
                status += "snow "
        if(len(status) < 1):
            status = "sun "
        if(isinstance(meteo.cloudiness, float)): 
            if(meteo.cloudiness > 50):
                status += "cloudy"
    except:
        pass
    finally:
        return status
