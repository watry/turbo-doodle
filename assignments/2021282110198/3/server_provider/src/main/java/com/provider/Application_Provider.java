package com.provider;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;

@SpringBootApplication(scanBasePackages="com.provider.controller")
@EnableEurekaClient
public class Application_Provider {
    public static void main(String[] args){
        SpringApplication.run(Application_Provider.class);
    }
}
