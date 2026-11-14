package com.enrichmeai.wre.patterns.adapter;

/**
 * Code we cannot change: an old library that reports tenths of a degree Fahrenheit.
 */
public class LegacyFahrenheitSensor {

    private final int tenthsFahrenheit;

    public LegacyFahrenheitSensor(int tenthsFahrenheit) {
        this.tenthsFahrenheit = tenthsFahrenheit;
    }

    public int readTenthsOfFahrenheit() {
        return tenthsFahrenheit;
    }
}
