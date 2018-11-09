package com.arturwagner.game2d;

import java.awt.Graphics;
import java.awt.Color;
import java.util.Random;

public class Player extends GameObject{
    Random r = new Random();
    public Player(int x, int y, ID id){
        super(x, y, id);
        setVelX(getVelX() + r.nextInt(7) - 3);
        setVelY(getVelY() + r.nextInt(7) - 3);
    }

    public void tick(){
        x += velX;
        y += velY;
    }
    public void render(Graphics g) {
        g.setColor(Color.darkGray);
        g.fillRect(x, y, 32, 32);
    }
}
