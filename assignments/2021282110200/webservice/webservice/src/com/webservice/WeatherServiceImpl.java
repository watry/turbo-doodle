package com.webservice;

import javax.jws.WebMethod;
import javax.jws.WebService;
@WebService
public interface WeatherServiceImpl {
    @WebMethod
    String getWeatherByCityname(String name);
}
