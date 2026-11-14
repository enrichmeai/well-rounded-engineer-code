package com.enrichmeai.wre.javatour;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.time.DayOfWeek;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.EnumSource;

class SwitchExpressionsTest {

    @Test
    void saturdayIsTheWeekend() {
        assertEquals("weekend", SwitchExpressions.kindOfDay(DayOfWeek.SATURDAY));
        assertEquals("weekday", SwitchExpressions.kindOfDay(DayOfWeek.WEDNESDAY));
    }

    @ParameterizedTest
    @EnumSource(DayOfWeek.class)
    void countsTheLettersOfEveryDay(DayOfWeek day) {
        assertEquals(day.name().length(), SwitchExpressions.lettersIn(day));
    }
}
