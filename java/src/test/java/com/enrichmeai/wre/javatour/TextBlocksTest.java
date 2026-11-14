package com.enrichmeai.wre.javatour;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class TextBlocksTest {

    @Test
    void theTextBlockKeepsItsShapeButNotTheCodeIndentation() {
        String expected = "{\n  \"greeting\": \"Hello, Ada!\"\n}\n";
        assertEquals(expected, TextBlocks.greetingJson("Ada"));
    }
}
