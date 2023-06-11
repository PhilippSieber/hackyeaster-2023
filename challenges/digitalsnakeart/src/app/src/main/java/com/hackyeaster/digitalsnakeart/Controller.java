package com.hackyeaster.digitalsnakeart;

import java.io.ByteArrayInputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.yaml.snakeyaml.Yaml;

@org.springframework.stereotype.Controller
public class Controller {

    @Autowired
    private Environment env;

    @GetMapping("/")
    public String index(Model model) {
        return "index";
    }

    @GetMapping("/art")
    public String path(Model model, @RequestParam(name = "art") String art) {
        SnakeService.initialize(env);
        SnakeArt result = parse(art);
        if (result == null) {
            return "fail";
        }
        model.addAttribute("name", result.getName());
        model.addAttribute("image64", result.getImage().getBase64String());
        model.addAttribute("source", result.getSource());
        model.addAttribute("resolution", result.getResolution());
        return "art";
    }

    private SnakeArt parse(String string) {
        try {
            byte[] yml = Base64.getDecoder().decode(string);
            InputStreamReader reader = new InputStreamReader(new ByteArrayInputStream(yml), StandardCharsets.UTF_8);
            return new Yaml().loadAs(reader, SnakeArt.class);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

}
