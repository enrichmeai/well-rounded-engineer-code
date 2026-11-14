package com.enrichmeai.wre.patterns.adapter;

/** Our code: it only knows about {@link Thermometer}. */
public final class HeatingController {

    private final Thermometer thermometer;
    private final double targetCelsius;

    public HeatingController(Thermometer thermometer, double targetCelsius) {
        this.thermometer = thermometer;
        this.targetCelsius = targetCelsius;
    }

    public boolean shouldHeat() {
        return thermometer.celsius() < targetCelsius;
    }
}
