package com.arturwagner.the_game;

import javax.swing.*;
import java.awt.*;

public class game extends Canvas {
    public static void main(String[] args) {
        JFrame frame = new JFrame("The game");
        Canvas canvas = new game();
        canvas.setSize(400, 400);
        frame.add(canvas);
        frame.pack();
        frame.setVisible(true);
    }
}
