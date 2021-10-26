package Weather;

import javax.jws.WebService;

@WebService
public class WeatherService implements WeatherServiceImpl {

    @Override
    public String getWeatherByCityname(String name) {
        return name + "天气晴朗！";
    }
}
