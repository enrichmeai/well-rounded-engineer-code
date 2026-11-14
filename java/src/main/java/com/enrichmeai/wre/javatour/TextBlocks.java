package com.enrichmeai.wre.javatour;

/**
 * Java 15: text blocks.
 *
 * <p>Three double quotes start a multi-line string. The common indentation is removed, so the
 * text can sit in line with the code, and you no longer need {@code \n} and {@code +} on every line.
 */
public final class TextBlocks {

    private TextBlocks() {
    }

    public static String greetingJson(String name) {
        return """
                {
                  "greeting": "Hello, %s!"
                }
                """.formatted(name);
    }
}
