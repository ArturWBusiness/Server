public class Test {
	public static void main(String[] args) {
		int candidate = 0;  // Number of the candidate used
		int x = 0;
		int y = 0;
		while (x < 5) {
			if (candidate == 0) {
				y = x - y;
			} else if (candidate == 1) {
				y += x;
			} else if (candidate == 2) {
				y += 2;
				if (y > 4) {y -= 1;};
			} else if (candidate == 3) {
				x += 1;
				y += x;
			} else if (candidate == 4) {
				if (y < 5) {
					x += 1;
					if (y < 3) {x -= 1;};
				};
				y += 2;
			};
			
			System.out.print(x + "" + y + " ");
			x += 1;
		};
	};
}