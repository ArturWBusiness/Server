package com.arturwagner.gameOfLife;

import java.util.Random;

public class game {

    private static int worldHeight = 30;
    private static int worldWidth = 50;
    private static Random r = new Random();
    private static String[][] world = new String[worldHeight][worldWidth];
    private static String[][] worldOut = new String[worldHeight][worldWidth];

    public static void main(String[] args) {
        newworld(0);

        world[12][12] = "X";
        world[12][13] = "X";
        world[12][11] = "X";
        world[11][12] = "X";

        while (true){
            render();
            try {
                Thread.sleep(250);
            }
            catch(InterruptedException ex) {
                Thread.currentThread().interrupt();
            }
            step();

        }
    }
    private static void newworld(double noise) {
        double deathChance = (noise) * 100;
        for (int y=0; y < worldHeight;y++) {
            for (int x=0; x < worldWidth;x++) {
                if (r.nextInt(100) + 1 <= deathChance) {
                    world[y][x] = "X";
                } else {
                    world[y][x] = " ";
                }
            }
        }
    }
    private static void step() {
        System.out.println("> Doing a step...");
        for (int y = 0; y < worldHeight; y++) {
            for (int x = 0; x < worldWidth; x++) {
                int neighbours = 0;
                for (int ny = -1; ny <= 1; ny++) {
                    for (int nx = -1; nx <= 1; nx++) {
                        if ((nx == 0) && (ny == 0)) {
                            continue;
                        }
                        try {
                            if ("X".equals(world[y + ny][x + nx])) {
                                neighbours += 1;
                            }
                        } catch (Throwable e) {
                            neighbours += 0;
                        }
                    }
                }
                if (world[y][x].equals("X")) {
                    if (neighbours == 3 || neighbours == 2 ){
                        worldOut[y][x] = "X";
                    } else {
                        worldOut[y][x] = " ";
                    }
                } else if (world[y][x].equals(" ")) {
                    if (neighbours == 3){
                        worldOut[y][x] = "X";
                    } else {
                        worldOut[y][x] = " ";
                    }
                }
            }
        }
        for (int y = 0; y < worldHeight; y++) {
            for (int x = 0; x < worldWidth; x++) {
                world[y][x] = worldOut[y][x];
            }
        }
    }

    private static void render() {
        System.out.println("> Rendering...");
        for (int y=0; y < worldHeight;y++) {
            for (int x = 0; x < worldWidth; x++) {
                System.out.print(world[y][x]);
            }
            System.out.println();
        }
    }
}
