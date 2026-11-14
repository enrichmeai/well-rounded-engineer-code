package com.enrichmeai.wre.patterns.observer;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.ArrayList;
import java.util.List;
import org.junit.jupiter.api.Test;

class PriceTickerTest {

    @Test
    void everySubscriberHearsAboutAChange() {
        var ticker = new PriceTicker();
        List<String> log = new ArrayList<>();
        List<String> alerts = new ArrayList<>();
        ticker.subscribe((symbol, oldPence, newPence) -> log.add(symbol + " " + oldPence + "->" + newPence));
        ticker.subscribe((symbol, oldPence, newPence) -> {
            if (newPence < oldPence * 0.9) {
                alerts.add(symbol + " fell more than 10%");
            }
        });

        ticker.update("ACME", 1_000);
        ticker.update("ACME", 850);

        assertEquals(List.of("ACME 1000->1000", "ACME 1000->850"), log);
        assertEquals(List.of("ACME fell more than 10%"), alerts);
    }

    @Test
    void anUnchangedPriceNotifiesNobody() {
        var ticker = new PriceTicker();
        List<Long> seen = new ArrayList<>();
        ticker.subscribe((symbol, oldPence, newPence) -> seen.add(newPence));
        ticker.update("ACME", 1_000);
        ticker.update("ACME", 1_000);
        assertEquals(List.of(1_000L), seen);
    }

    @Test
    void anUnsubscribedListenerHearsNothingMore() {
        var ticker = new PriceTicker();
        List<Long> seen = new ArrayList<>();
        Runnable unsubscribe = ticker.subscribe((symbol, oldPence, newPence) -> seen.add(newPence));
        ticker.update("ACME", 1_000);
        unsubscribe.run();
        ticker.update("ACME", 2_000);
        assertEquals(List.of(1_000L), seen);
    }
}
