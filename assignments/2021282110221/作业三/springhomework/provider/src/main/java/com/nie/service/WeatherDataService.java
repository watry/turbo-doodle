package com.nie.service;

import com.nie.pojo.WeatherResponse;
import org.springframework.stereotype.Service;


public interface WeatherDataService {

    WeatherResponse getDataByCityId(String CityId);

    WeatherResponse getDataByCityName(String cityName);

}
