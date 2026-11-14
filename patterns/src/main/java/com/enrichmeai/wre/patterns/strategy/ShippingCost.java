package com.enrichmeai.wre.patterns.strategy;

/**
 * Strategy: one interface, several interchangeable ways of doing the same job.
 *
 * <p>The checkout does not know how postage is worked out. It is handed a strategy and calls it.
 * Adding "next-day delivery" is a new class, not another branch in an if/else that every change
 * has to touch.
 */
@FunctionalInterface
public interface ShippingCost {

    /** The cost in pence of sending a parcel of the given weight in grams. */
    long pence(int grams);

    /** A flat rate whatever the weight. */
    static ShippingCost flat(long pence) {
        return grams -> pence;
    }

    /** A base price plus a price for every started kilogram. */
    static ShippingCost byWeight(long basePence, long pencePerKg) {
        return grams -> basePence + pencePerKg * ((grams + 999) / 1000);
    }

    /** Free above a threshold order value, otherwise the fallback strategy. Strategies compose. */
    static ShippingCost freeOver(long orderPence, long thresholdPence, ShippingCost otherwise) {
        return grams -> orderPence >= thresholdPence ? 0 : otherwise.pence(grams);
    }
}
