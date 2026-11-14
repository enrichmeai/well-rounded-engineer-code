package com.enrichmeai.wre.patterns.strategy;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class CheckoutTest {

    @Test
    void theSameCheckoutWorksWithAnyStrategy() {
        assertEquals(1_500 + 399, new Checkout(ShippingCost.flat(399)).total(1_500, 2_500));
        // 2,500 g is three started kilograms: 200 + 3 x 150
        assertEquals(1_500 + 650, new Checkout(ShippingCost.byWeight(200, 150)).total(1_500, 2_500));
    }

    @Test
    void strategiesCanBeCombined() {
        ShippingCost freeOverFifty = ShippingCost.freeOver(6_000, 5_000, ShippingCost.flat(399));
        assertEquals(6_000, new Checkout(freeOverFifty).total(6_000, 1_000));

        ShippingCost notEnough = ShippingCost.freeOver(1_000, 5_000, ShippingCost.flat(399));
        assertEquals(1_399, new Checkout(notEnough).total(1_000, 1_000));
    }

    @Test
    void aNewStrategyNeedsNoChangeToCheckout() {
        ShippingCost collectInStore = grams -> 0;
        assertEquals(1_000, new Checkout(collectInStore).total(1_000, 50_000));
    }
}
