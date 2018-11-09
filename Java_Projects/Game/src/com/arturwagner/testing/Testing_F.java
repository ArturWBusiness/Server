package com.arturwagner.testing;


public class Testing_F {
    public static void main(String[] args){
        int sum = 8;
        int[] list = new int[]{1,2,4,4};
        for(int i = 0; i < list.length; i++){
            for(int i2 = 0; i2 < list.length; i2++){
                if(i==i2){

                }else if(list[i]+list[i2]==sum){
                    System.out.println(list[i] + " + " + list[i2] + " = " + sum);
                }
            }
        }
    }
}
