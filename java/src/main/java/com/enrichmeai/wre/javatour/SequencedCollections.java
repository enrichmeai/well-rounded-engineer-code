package com.enrichmeai.wre.javatour;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.SequencedMap;

/**
 * Java 21: sequenced collections.
 *
 * <p>Lists, deques, {@code LinkedHashSet} and {@code LinkedHashMap} now share one way to reach
 * their first and last elements and to walk them backwards: {@code getFirst()}, {@code getLast()}
 * and {@code reversed()}. Before, it was {@code list.get(list.size() - 1)} for one and an iterator
 * loop for another.
 */
public final class SequencedCollections {

    private SequencedCollections() {
    }

    public static String firstAndLast(List<String> items) {
        return items.getFirst() + " .. " + items.getLast();
    }

    public static List<String> newestFirst(List<String> oldestFirst) {
        return oldestFirst.reversed();
    }

    /** The most recently added entry of an insertion-ordered map. */
    public static Map.Entry<String, Integer> latest(SequencedMap<String, Integer> scores) {
        return scores.lastEntry();
    }

    public static SequencedMap<String, Integer> scoresInOrder() {
        var scores = new LinkedHashMap<String, Integer>();
        scores.put("ada", 3);
        scores.put("bob", 5);
        scores.putFirst("zoe", 1);
        return scores;
    }
}
