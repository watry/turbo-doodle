package com.chlts.weather.controller;

import com.chlts.weather.dto.WeatherDto;
import com.chlts.weather.util.WeatherUtil;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

@RestController
public class WeatherController {

    @RequestMapping("/weather/{city}")
    public String weather(@PathVariable("city") String city) throws IOException {
        String url = "https://restapi.amap.com/v3/weather/weatherInfo?key=23aa57f0813a4796fb1ce28220fdc5bf&city="+city+"&extensions=base";
        URL serverUrl = new URL(url);
        HttpURLConnection connection = (HttpURLConnection) serverUrl.openConnection();
        connection.setRequestMethod("GET");
        if (connection.getResponseCode() != 200) {
            throw new RuntimeException(
                    "HTTP GET Request Failed with Error code : "
                            + connection.getResponseCode());
        }
        BufferedReader responseBuffer = new BufferedReader(
                new InputStreamReader((connection.getInputStream())));
        String output;
        String res="";
        while ((output = responseBuffer.readLine()) != null) {
            res=output;
        }
        WeatherDto weatherDto= WeatherUtil.toWeatherDto(res);
        connection.disconnect();
        return weatherDto.toString();
    }

}
