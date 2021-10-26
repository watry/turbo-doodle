package com.chlts.eureka;

import lombok.extern.log4j.Log4j2;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;
import org.springframework.core.env.Environment;

@SpringBootApplication
@EnableEurekaServer
@Log4j2
public class EurekaApplication {

    public static void main(String[] args) {
        SpringApplication application=new SpringApplication(EurekaApplication.class);
        Environment environment=application.run(args).getEnvironment();
        log.info("启动成功");
        log.info("注册中心地址：\thttp://127.0.0.1:{}",environment.getProperty("server.port"));
    }

}
