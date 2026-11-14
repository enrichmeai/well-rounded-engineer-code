package com.enrichmeai.wre.javatour;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTimeout;

import java.time.Duration;
import org.junit.jupiter.api.Test;

class VirtualThreadsTest {

    @Test
    void tenThousandSleepingTasksFinishQuickly() {
        // 10,000 tasks x 100 ms would be over 16 minutes one at a time. On virtual threads they wait together.
        int finished = assertTimeout(Duration.ofSeconds(20),
                () -> VirtualThreads.runConcurrently(10_000, Duration.ofMillis(100)));
        assertEquals(10_000, finished);
    }

    @Test
    void aVirtualThreadCanHaveAName() throws InterruptedException {
        assertEquals("worker-1", VirtualThreads.nameOfVirtualThread());
    }
}
