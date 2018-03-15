package com;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		// List<String> string = new ArrayList<String>();
        // string.add("item");
		List<String> world = Arrays.asList("Hello", "World");
		Scanner in = new Scanner(System.in);
		System.out.println(in.nextLine() + world);
		in.close();
	}

}
