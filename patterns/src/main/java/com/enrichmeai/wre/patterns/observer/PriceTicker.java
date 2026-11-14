package com.enrichmeai.wre.patterns.observer;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.CopyOnWriteArrayList;

/**
 * Observer: the subject keeps a list of listeners and tells each of them when something changes.
 *
 * <p>The ticker does not know who is listening (a chart, an alert, a log). Listeners subscribe and
 * unsubscribe at run time, and the ticker never has to change when a new kind of listener appears.
 */
public final class PriceTicker {

    /** The observer interface. */
    @FunctionalInterface
    public interface PriceListener {
        void priceChanged(String symbol, long oldPence, long newPence);
    }

    private final List<PriceListener> listeners = new CopyOnWriteArrayList<>();
    private final Map<String, Long> prices = new HashMap<>();

    /** Subscribes a listener and returns a handle that unsubscribes it. */
    public Runnable subscribe(PriceListener listener) {
        listeners.add(listener);
        return () -> listeners.remove(listener);
    }

    public void update(String symbol, long newPence) {
        Long old = prices.put(symbol, newPence);
        if (old != null && old == newPence) {
            return; // nothing changed, so nobody is told
        }
        long oldPence = old == null ? newPence : old;
        for (PriceListener listener : listeners) {
            listener.priceChanged(symbol, oldPence, newPence);
        }
    }
}
