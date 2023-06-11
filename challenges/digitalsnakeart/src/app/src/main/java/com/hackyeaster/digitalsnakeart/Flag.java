package com.hackyeaster.digitalsnakeart;

public class Flag extends Image {

    public Flag(Code code) {
        if (code.isCorrect()) {
            this.base64String = SnakeService.loadFlag();
        } else {
            this.base64String = SnakeService.load("snake_no_access");
        }
    }
}
