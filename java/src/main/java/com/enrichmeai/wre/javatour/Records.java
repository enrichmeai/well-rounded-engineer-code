package com.enrichmeai.wre.javatour;

/**
 * Java 16: records, and pattern matching for {@code instanceof}.
 *
 * <p>A record is a class whose job is to carry data. Java writes the constructor, the accessors,
 * {@code equals}, {@code hashCode} and {@code toString} for you. A compact constructor is where
 * you check the values.
 */
public final class Records {

    private Records() {
    }

    public record Money(long pence, String currency) {
        public Money {
            if (pence < 0) {
                throw new IllegalArgumentException("pence must not be negative: " + pence);
            }
            if (currency == null || currency.length() != 3) {
                throw new IllegalArgumentException("currency must be a three-letter code: " + currency);
            }
        }

        public Money plus(Money other) {
            if (!currency.equals(other.currency)) {
                throw new IllegalArgumentException("cannot add " + other.currency + " to " + currency);
            }
            return new Money(pence + other.pence, currency);
        }
    }

    /**
     * Pattern matching for {@code instanceof}: the test and the cast are one step, and
     * {@code money} is only in scope where the test passed.
     */
    public static String describe(Object value) {
        if (value instanceof Money money && money.pence() == 0) {
            return "nothing";
        }
        if (value instanceof Money money) {
            return money.pence() / 100 + "." + String.format("%02d", money.pence() % 100) + " " + money.currency();
        }
        return "not money";
    }
}
