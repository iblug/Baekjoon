import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        String s;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            s = br.readLine();
            if (s == null) {
                break;
            }
            System.out.println(s);
        }
    }
}