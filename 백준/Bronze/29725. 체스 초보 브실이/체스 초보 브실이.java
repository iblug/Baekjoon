import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        int w = 0;
        int b = 0;

        String s;
        char c;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 8; i++) {
            s = br.readLine();
            for (int j = 0; j < 8; j++) {
                c = s.charAt(j);
                if (c == 'K' || c == 'k' || c == '.') {
                    continue;
                } else if (c == 'P') {
                    w++;
                } else if (c == 'N' || c == 'B') {
                    w += 3;
                } else if (c == 'R') {
                    w += 5;
                } else if (c == 'Q') {
                    w += 9;
                } else if (c == 'p') {
                    b++;
                } else if (c == 'n' || c == 'b') {
                    b += 3;
                } else if (c == 'r') {
                    b += 5;
                } else if (c == 'q') {
                    b += 9;
                }
            }
        }

        System.out.println(w - b);
    }
}