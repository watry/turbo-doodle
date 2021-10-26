package com.chlts.loaction;

import lombok.extern.log4j.Log4j2;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;
import org.springframework.core.env.Environment;

@SpringBootApplication
@Log4j2
@EnableEurekaClient
public class LocationApplication {

    public static void main(String[] args) {
        SpringApplication application=new SpringApplication(LocationApplication.class);
        Environment environment=application.run(args).getEnvironment();
        log.info("启动成功");
        log.info("Location地址：\thttp://127.0.0.1:{}",environment.getProperty("server.port"));
    }

}
