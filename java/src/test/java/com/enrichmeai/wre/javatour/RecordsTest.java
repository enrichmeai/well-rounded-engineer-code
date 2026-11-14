package com.enrichmeai.wre.javatour;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import com.enrichmeai.wre.javatour.Records.Money;
import org.junit.jupiter.api.Test;

class RecordsTest {

    @Test
    void recordsWithTheSameValuesAreEqual() {
        assertEquals(new Money(150, "GBP"), new Money(150, "GBP"));
        assertEquals("Money[pence=150, currency=GBP]", new Money(150, "GBP").toString());
    }

    @Test
    void theCompactConstructorRejectsBadValues() {
        assertThrows(IllegalArgumentException.class, () -> new Money(-1, "GBP"));
        assertThrows(IllegalArgumentException.class, () -> new Money(1, "pounds"));
    }

    @Test
    void addsMoneyOfTheSameCurrencyOnly() {
        assertEquals(new Money(250, "GBP"), new Money(100, "GBP").plus(new Money(150, "GBP")));
        assertThrows(IllegalArgumentException.class, () -> new Money(1, "GBP").plus(new Money(1, "EUR")));
    }

    @Test
    void instanceofBindsAVariable() {
        assertEquals("12.05 GBP", Records.describe(new Money(1205, "GBP")));
        assertEquals("nothing", Records.describe(new Money(0, "GBP")));
        assertEquals("not money", Records.describe("12.05"));
    }
}
