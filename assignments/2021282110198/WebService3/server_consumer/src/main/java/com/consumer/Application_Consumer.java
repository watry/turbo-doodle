package com.consumer;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication(scanBasePackages="com.consumer.controller")
public class Application_Consumer {
    public static void main(String[] args){
        SpringApplication.run(Application_Consumer.class);
    }
}

