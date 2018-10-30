class Movie {
	String title;
	String genre;
	int rating;
	
	void playIt() {
		System.out.println("Playing the \"" + title + "\"");
	}
}

public class MovieTestDrive {
	public static void main(String[] args) {
		Movie one = new Movie();
		one.title = "Angels of Death";
		one.genre = "Thriller";
		one.rating = 7;
		one.playIt();
	}
}