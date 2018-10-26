package com.arturwagner;
import javafx.util.Pair;

import java.awt.event.*;
import java.awt.Robot;
import java.awt.PointerInfo;
import java.awt.MouseInfo;
import java.awt.Point;
import java.awt.KeyEventDispatcher;
import java.awt.KeyboardFocusManager;
public class Main {

    public static void main(String args[]) {
        while (true) {
            int[] cords = mouse_pos();
            System.out.println("x:" + cords[0] + " y:" + cords[1]);
        }
    }

    private static int[] mouse_pos() {
        PointerInfo a = MouseInfo.getPointerInfo();
        Point b = a.getLocation();
        int x = (int) b.getX();
        int y = (int) b.getY();
        int arr[] = new int[2];
        arr[0] = x;
        arr[1] = y;
        return arr;

    }
    private static void click(int x, int y) {
        Robot bot = null;
        try {
            bot = new Robot();
        } catch (Exception failed) {
            System.err.println("Failed instantiating Robot: " + failed);
        }
        int mask = InputEvent.BUTTON1_DOWN_MASK;
        bot.mouseMove(x, y);
        bot.mousePress(mask);
        bot.mouseRelease(mask);

    }
}

