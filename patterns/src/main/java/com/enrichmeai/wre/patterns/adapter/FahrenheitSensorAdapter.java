package com.enrichmeai.wre.patterns.adapter;

import java.util.Objects;

/**
 * Adapter: makes an existing class fit the interface our code expects, without changing either.
 *
 * <p>The conversion lives in one small class. The rest of the code keeps talking to a
 * {@link Thermometer}, and never learns that the sensor underneath speaks Fahrenheit.
 */
public final class FahrenheitSensorAdapter implements Thermometer {

    private final LegacyFahrenheitSensor sensor;

    public FahrenheitSensorAdapter(LegacyFahrenheitSensor sensor) {
        this.sensor = Objects.requireNonNull(sensor);
    }

    @Override
    public double celsius() {
        double fahrenheit = sensor.readTenthsOfFahrenheit() / 10.0;
        return (fahrenheit - 32) * 5 / 9;
    }
}
