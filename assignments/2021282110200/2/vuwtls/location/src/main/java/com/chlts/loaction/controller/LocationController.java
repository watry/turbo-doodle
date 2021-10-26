package com.chlts.loaction.controller;

import com.alibaba.fastjson.JSONObject;
import com.chlts.loaction.util.CharChange;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

@RestController
public class LocationController {

    @RequestMapping("/location/{ip}")
    public String location(@PathVariable("ip") String ip) throws IOException {
        String url = "https://api.map.baidu.com/location/ip?ak=ctjtLHtI40FAN1BGmTDgHEkXhDq5dvT8&ip="+ip+"&coor=bd09ll";
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
        String cityUnicode=res.substring(res.indexOf("\"city\":\"")+8,res.indexOf("\",\"city_code\""));
        String cityCn=CharChange.unicodeToCn(cityUnicode);
        connection.disconnect();
        return cityCn;
    }

}
