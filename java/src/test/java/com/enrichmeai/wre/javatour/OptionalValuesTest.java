package com.enrichmeai.wre.javatour;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Map;
import java.util.Optional;
import org.junit.jupiter.api.Test;

class OptionalValuesTest {

    private final OptionalValues directory = new OptionalValues(Map.of(
            "ada", "ada@example.org",
            "bob", "not-an-email"));

    @Test
    void aKnownUserHasAnEmail() {
        assertEquals(Optional.of("ada@example.org"), directory.emailOf("ada"));
    }

    @Test
    void anUnknownUserHasAnEmptyOptionalNotNull() {
        assertTrue(directory.emailOf("carol").isEmpty());
    }

    @Test
    void domainIsReadFromTheEmail() {
        assertEquals("example.org", directory.domainOf("ada"));
    }

    @Test
    void domainFallsBackWhenTheEmailIsMissingOrInvalid() {
        assertEquals("unknown", directory.domainOf("carol"));
        assertEquals("unknown", directory.domainOf("bob"));
    }
}
