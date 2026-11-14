package com.enrichmeai.wre.javatour;

import java.time.Duration;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

/**
 * Java 21: virtual threads.
 *
 * <p>A virtual thread is cheap: the JDK, not the operating system, schedules it, and a thread that
 * is waiting (on a sleep, a socket, a file) gives its carrier back. So you can write plain,
 * blocking code and still run thousands of tasks at once.
 */
public final class VirtualThreads {

    private VirtualThreads() {
    }

    /**
     * Runs {@code tasks} tasks that each wait {@code pause}, one virtual thread per task, and returns
     * how many finished. With platform threads in a small pool this would take tasks x pause.
     */
    public static int runConcurrently(int tasks, Duration pause) throws InterruptedException, ExecutionException {
        try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
            List<Future<Boolean>> results = new ArrayList<>();
            for (int i = 0; i < tasks; i++) {
                results.add(executor.submit(() -> {
                    Thread.sleep(pause);
                    return Thread.currentThread().isVirtual();
                }));
            }
            int virtual = 0;
            for (Future<Boolean> result : results) {
                if (result.get()) {
                    virtual++;
                }
            }
            return virtual;
        }
    }

    /** Starts a single virtual thread with a name and waits for it. */
    public static String nameOfVirtualThread() throws InterruptedException {
        var seen = new String[1];
        Thread thread = Thread.ofVirtual().name("worker-1").start(() -> seen[0] = Thread.currentThread().getName());
        thread.join();
        return seen[0];
    }
}
