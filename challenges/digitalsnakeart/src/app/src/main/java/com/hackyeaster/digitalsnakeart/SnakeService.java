package com.hackyeaster.digitalsnakeart;

import org.springframework.core.env.Environment;
import org.springframework.stereotype.Service;

@Service
public class SnakeService {

    private static Environment env;

    static void initialize(Environment environment) {
        if (env == null) {
            env = environment;
        }
    }

    static short getSecretCode() {
        return env != null ? new Short(env.getProperty("secret.code")) : -1;
    }

    static String load(String name) {
        if (name != null && name.startsWith("snake") && name.length() <= 30) {
            return env.getProperty("image." + name);
        }
        return env.getProperty("image.notfound");
    }

    static String loadFlag() {
        return env.getProperty("image.flag");
    }

}
