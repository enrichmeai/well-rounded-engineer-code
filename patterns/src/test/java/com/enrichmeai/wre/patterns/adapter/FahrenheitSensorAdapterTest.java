package com.enrichmeai.wre.patterns.adapter;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class FahrenheitSensorAdapterTest {

    @Test
    void convertsTheLegacyReadingToCelsius() {
        assertEquals(0.0, new FahrenheitSensorAdapter(new LegacyFahrenheitSensor(320)).celsius(), 1e-9);
        assertEquals(100.0, new FahrenheitSensorAdapter(new LegacyFahrenheitSensor(2120)).celsius(), 1e-9);
        assertEquals(20.0, new FahrenheitSensorAdapter(new LegacyFahrenheitSensor(680)).celsius(), 1e-9);
    }

    @Test
    void ourCodeWorksWithTheOldSensorThroughTheAdapter() {
        var cold = new HeatingController(new FahrenheitSensorAdapter(new LegacyFahrenheitSensor(590)), 18);
        var warm = new HeatingController(new FahrenheitSensorAdapter(new LegacyFahrenheitSensor(700)), 18);
        assertTrue(cold.shouldHeat()); // 59.0 F is 15 C
        assertFalse(warm.shouldHeat()); // 70.0 F is about 21.1 C
    }

    @Test
    void andWithAnyOtherThermometerToo() {
        assertTrue(new HeatingController(() -> 12.5, 18).shouldHeat());
    }
}
