package com.enrichmeai.wre.javatour;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.Test;

class SequencedCollectionsTest {

    @Test
    void readsTheFirstAndLastElement() {
        assertEquals("a .. c", SequencedCollections.firstAndLast(List.of("a", "b", "c")));
    }

    @Test
    void reversedIsAReverseOrderedView() {
        assertEquals(List.of("c", "b", "a"), SequencedCollections.newestFirst(List.of("a", "b", "c")));
    }

    @Test
    void putFirstMovesAnEntryToTheFrontOfAnOrderedMap() {
        var scores = SequencedCollections.scoresInOrder();
        assertEquals(List.of("zoe", "ada", "bob"), List.copyOf(scores.sequencedKeySet()));
        assertEquals(Map.entry("bob", 5), SequencedCollections.latest(scores));
    }
}
