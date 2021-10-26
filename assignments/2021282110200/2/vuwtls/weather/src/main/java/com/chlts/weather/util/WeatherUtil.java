package com.chlts.weather.util;

import com.chlts.weather.dto.WeatherDto;

import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;

public class WeatherUtil {

    public static WeatherDto toWeatherDto(String s){
        Class clazz=WeatherDto.class;
        try {
            WeatherDto weatherDto=(WeatherDto) clazz.getConstructor().newInstance();
            for (Field field : clazz.getDeclaredFields()) {
                field.setAccessible(true);
                String fieldName=field.getName();
                String ss="\""+fieldName+"\":\"";
                int start=s.indexOf(ss)+ss.length();
                int end=start;
                while (s.charAt(end)!='\"') end++;
                String value=s.substring(start,end);
                field.set(weatherDto,value);
            }
            return weatherDto;
        } catch (InstantiationException e) {
            throw new RuntimeException();
        } catch (IllegalAccessException e) {
            throw new RuntimeException();
        } catch (InvocationTargetException e) {
            throw new RuntimeException();
        } catch (NoSuchMethodException e) {
            throw new RuntimeException();
        }
    }

}
