package com.enrichmeai.wre.javatour;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.Test;

class LocalVariableTypeInferenceTest {

    @Test
    void countsWordsIgnoringCase() {
        assertEquals(Map.of("the", 2, "cat", 1, "sat", 1), LocalVariableTypeInference.wordCounts("The cat sat  the"));
    }

    @Test
    void varWorksForLambdaParametersToo() {
        assertEquals(List.of("a", "b"), LocalVariableTypeInference.trimmedAll(List.of("  a ", "b  ")));
    }
}
