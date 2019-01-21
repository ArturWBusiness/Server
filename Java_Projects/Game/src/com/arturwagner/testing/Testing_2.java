package com.arturwagner.testing;

import java.util.ArrayList;

public class Testing_2 {
    public void main(String args[]) {
        ArrayList<String> array = new ArrayList<String>();
        array.add("I");
        array.add("Love");
        array.add("To");
        array.add("Watch");

        array.add("Anime");

        int largestString = array.get(0).length();

        for(int i = 0; i < array.size(); i++) {
            if(array.get(i).length() > largestString) {
                largestString = array.get(i).length();
            }
        }
        System.out.println("############################");
    }

}
