package com.enrichmeai.wre.javatour;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Java 10: {@code var} for local variables.
 *
 * <p>The compiler works out the type from the right-hand side. The variable is still strongly
 * typed: {@code var counts} below is a {@code HashMap<String, Integer>} and nothing else. Use it
 * when the type is obvious from the line; spell the type out when it is not.
 */
public final class LocalVariableTypeInference {

    private LocalVariableTypeInference() {
    }

    /** Counts how often each word appears. */
    public static Map<String, Integer> wordCounts(String text) {
        var counts = new HashMap<String, Integer>();
        for (var word : text.toLowerCase().split("\\s+")) {
            if (!word.isEmpty()) {
                counts.merge(word, 1, Integer::sum);
            }
        }
        return counts;
    }

    /** Java 11 also lets you write {@code var} for lambda parameters. */
    public static List<String> trimmedAll(List<String> lines) {
        var result = new ArrayList<String>();
        lines.forEach((var line) -> result.add(line.strip()));
        return result;
    }
}
