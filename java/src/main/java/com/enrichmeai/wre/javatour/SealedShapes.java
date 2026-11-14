package com.enrichmeai.wre.javatour;

/**
 * Java 17: sealed types. Java 21: pattern matching for switch, with record patterns.
 *
 * <p>{@code sealed ... permits} lists every allowed subtype. Because the compiler knows the full
 * list, a switch over a {@code Shape} needs no {@code default}: add a fourth shape and every switch
 * that forgot it stops compiling. Record patterns take a record apart in the {@code case} itself.
 */
public final class SealedShapes {

    private SealedShapes() {
    }

    public sealed interface Shape permits Circle, Square, Rectangle {
    }

    public record Circle(double radius) implements Shape {
    }

    public record Square(double side) implements Shape {
    }

    public record Rectangle(double width, double height) implements Shape {
    }

    public static double area(Shape shape) {
        return switch (shape) {
            case Circle(double radius) -> Math.PI * radius * radius;
            case Square(double side) -> side * side;
            case Rectangle(double width, double height) -> width * height;
        };
    }

    /** A guard ({@code when}) refines a case. */
    public static String describe(Shape shape) {
        return switch (shape) {
            case Rectangle(double width, double height) when width == height -> "a square in disguise";
            case Rectangle r -> "a rectangle";
            case Square s -> "a square";
            case Circle c -> "a circle";
        };
    }
}
