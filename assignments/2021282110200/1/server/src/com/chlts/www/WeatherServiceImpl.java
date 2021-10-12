package com.chlts.www;

import javax.jws.WebMethod;
import javax.jws.WebService;

@WebService
public interface WeatherServiceImpl {

    @WebMethod
    String getWeatherByCityname(String name);

}