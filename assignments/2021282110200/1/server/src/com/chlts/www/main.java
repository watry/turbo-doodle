package com.chlts.www;

import javax.xml.ws.Endpoint;

public class main {

    public static void main(String[] args) {
        //发布天气服务，这里只是简单的测试
        Endpoint.publish("http://localhost:8085/ws_server/weather", new WeatherService());
        System.out.println("发布天气服务成功...");
    }
}