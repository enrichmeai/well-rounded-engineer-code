package com.enrichmeai.wre.patterns.strategy;

import java.util.Objects;

/** The context: it holds a strategy and uses it, without knowing which one it is. */
public final class Checkout {

    private final ShippingCost shipping;

    public Checkout(ShippingCost shipping) {
        this.shipping = Objects.requireNonNull(shipping);
    }

    public long total(long itemsPence, int parcelGrams) {
        return itemsPence + shipping.pence(parcelGrams);
    }
}
