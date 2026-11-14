package com.enrichmeai.wre.javatour;

import java.time.DayOfWeek;

/**
 * Java 14: switch expressions.
 *
 * <p>A switch can now return a value. The arrow form has no fall-through, so there is no
 * {@code break} to forget, and the compiler checks that every enum constant is covered.
 */
public final class SwitchExpressions {

    private SwitchExpressions() {
    }

    public static String kindOfDay(DayOfWeek day) {
        return switch (day) {
            case SATURDAY, SUNDAY -> "weekend";
            case MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY -> "weekday";
        };
    }

    /** {@code yield} returns a value from a block inside a switch expression. */
    public static int lettersIn(DayOfWeek day) {
        return switch (day) {
            case MONDAY, FRIDAY, SUNDAY -> 6;
            case TUESDAY -> 7;
            default -> {
                String name = day.name();
                yield name.length();
            }
        };
    }
}
