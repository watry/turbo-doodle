package com.nie.pojo;

import lombok.Data;
import org.springframework.beans.factory.annotation.Autowired;

import javax.xml.ws.Service;

@Data
public class WeatherResponse {
    private Weather data;
    private Integer status;
    private String desc;

}
