package com.hackyeaster.digitalsnakeart;

public class Code {

    private final short code;

    public Code(short code) {
        this.code = code;
    }

    public boolean isCorrect() {
        return (code > 0 && code < 500 && code == SnakeService.getSecretCode());
    }

}
