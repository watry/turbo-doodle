package com.chlts.unit.controller;

import com.chlts.loaction.controller.LocationController;
import com.chlts.weather.controller.WeatherController;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;

@RestController
public class UnitController {

    LocationController locationController;
    WeatherController weatherController;

    public UnitController(LocationController locationController, WeatherController weatherController) {
        this.locationController = locationController;
        this.weatherController = weatherController;
    }

    @RequestMapping("/searchWeatherByIp/{ip}")
    public String searchWeatherByIp(@PathVariable("ip") String ip) throws IOException {
        String city=locationController.location(ip);
        String weather=weatherController.weather(city);
        return weather;
    }
}
