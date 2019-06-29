package com.arturwagner;


import java.net.URL;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class Main{
	
	private static int HEIGHT = 400;
	private static int WIDTH = 400;
	
	public static void main(String[] args){ 
		
		JFrame window = new JFrame("A JFrame");
	    window.setSize(WIDTH, HEIGHT);

	    window.setLocation(300,200);
	    URL imagePath = Main.class.getResource(
	    	"/resources/anime.jpg"
	    );
	    ImageIcon icon = new ImageIcon(imagePath);
	    JLabel label = new JLabel(icon);
	    window.add(label);
	    
	    // Application closes when user clicks the "X" button.
	    window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	    window.pack();
	    window.setVisible(true);
	}
}
