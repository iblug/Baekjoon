import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	private BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		String n = br.readLine();

        long r = 0;
        for(int i = 0 ; i<n.length(); i++) {
            r = (r * 10 + (n.charAt(i) - '0')) % 20000303;
        }
        System.out.println(r);
	}
}