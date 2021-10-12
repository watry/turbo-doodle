package com.webservice;

public class ClientTest {
    public static void main(String[] args) {
        WeatherServiceService factory = new WeatherServiceService();
        WeatherService servicePort = factory.getWeatherServicePort();
        String weather = servicePort.getWeatherByCityname("深圳");
        System.out.println(weather);
    }
}
