package com.enrichmeai.wre.javatour;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.Test;

class LambdasAndStreamsTest {

    @Test
    void sumsOnlyTheEvenNumbers() {
        assertEquals(12, LambdasAndStreams.sumOfEvens(List.of(1, 2, 3, 4, 5, 6)));
    }

    @Test
    void anEmptyListSumsToZero() {
        assertEquals(0, LambdasAndStreams.sumOfEvens(List.of()));
    }

    @Test
    void keepsLongWordsAndShoutsThem() {
        List<String> result = LambdasAndStreams.shout(List.of("hi", "hello", "hey", "welcome"), w -> w.length() > 3);
        assertEquals(List.of("HELLO", "WELCOME"), result);
    }

    @Test
    void groupsWordsByFirstLetter() {
        Map<Character, List<String>> groups = LambdasAndStreams.byFirstLetter(List.of("apple", "banana", "avocado"));
        assertEquals(List.of("apple", "avocado"), groups.get('a'));
        assertEquals(List.of("banana"), groups.get('b'));
    }
}
