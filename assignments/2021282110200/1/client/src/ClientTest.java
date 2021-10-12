import com.chlts.WeatherService;
import com.chlts.WeatherServiceService;

public class ClientTest {
    public static void main(String[] args) {
        WeatherServiceService factory = new WeatherServiceService();
        WeatherService servicePort = factory.getWeatherServicePort();
        String weather = servicePort.getWeatherByCityname("武汉");
        System.out.println(weather);
    }
}
