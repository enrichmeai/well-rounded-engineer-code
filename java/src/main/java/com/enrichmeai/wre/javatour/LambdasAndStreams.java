package com.enrichmeai.wre.javatour;

import java.util.List;
import java.util.Map;
import java.util.function.Predicate;
import java.util.stream.Collectors;

/**
 * Java 8: lambdas and the Stream API.
 *
 * <p>A lambda is a short function you can pass around. A stream is a pipeline over a collection:
 * filter, map, then collect. Before Java 8 each of these methods would have been a loop.
 */
public final class LambdasAndStreams {

    private LambdasAndStreams() {
    }

    /** The sum of the even numbers in the list. */
    public static int sumOfEvens(List<Integer> numbers) {
        return numbers.stream()
                .filter(n -> n % 2 == 0)
                .mapToInt(Integer::intValue)
                .sum();
    }

    /** The words that pass the test, upper-cased, in their original order. */
    public static List<String> shout(List<String> words, Predicate<String> keep) {
        return words.stream()
                .filter(keep)
                .map(String::toUpperCase)
                .collect(Collectors.toList());
    }

    /** Groups words by their first letter, e.g. {a=[apple, avocado], b=[banana]}. */
    public static Map<Character, List<String>> byFirstLetter(List<String> words) {
        return words.stream()
                .collect(Collectors.groupingBy(word -> word.charAt(0)));
    }
}
