package com.hackyeaster.digitalsnakeart;

public class Image {

    protected String base64String;

    public String getBase64String() {
        if (base64String == null) {
            return SnakeService.load("fail");
        }
        return base64String;
    }

    protected Image() {
    }

    public Image(String name) {
        this.base64String = SnakeService.load(name);
    }
}
