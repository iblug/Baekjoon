import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		switch (System.in.read()) {
		case 'M':
			System.out.print("MatKor");
			break;
		case 'W':
			System.out.print("WiCys");
			break;
		case 'C':
			System.out.print("CyKor");
			break;
		case 'A':
			System.out.print("AlKor");
			break;
		case '$':
			System.out.print("$clear");
			break;
		}
	}
}