package com.enrichmeai.wre.javatour;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import com.enrichmeai.wre.javatour.SealedShapes.Circle;
import com.enrichmeai.wre.javatour.SealedShapes.Rectangle;
import com.enrichmeai.wre.javatour.SealedShapes.Shape;
import com.enrichmeai.wre.javatour.SealedShapes.Square;
import org.junit.jupiter.api.Test;

class SealedShapesTest {

    @Test
    void computesTheAreaOfEachShape() {
        assertEquals(Math.PI, SealedShapes.area(new Circle(1)), 1e-9);
        assertEquals(9, SealedShapes.area(new Square(3)), 1e-9);
        assertEquals(6, SealedShapes.area(new Rectangle(2, 3)), 1e-9);
    }

    @Test
    void theGuardCatchesARectangleWithEqualSides() {
        assertEquals("a square in disguise", SealedShapes.describe(new Rectangle(2, 2)));
        assertEquals("a rectangle", SealedShapes.describe(new Rectangle(2, 3)));
    }

    @Test
    void theInterfaceListsExactlyThePermittedSubtypes() {
        assertArrayEquals(new Class<?>[] {Circle.class, Square.class, Rectangle.class},
                Shape.class.getPermittedSubclasses());
    }
}
