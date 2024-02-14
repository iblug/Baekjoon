import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static String kan(int l) {
        if (l == 0) {
            return "-";
        }
        return kan(l - 1) + " ".repeat((int) Math.pow(3, l-1)) + kan(l - 1);
    }

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            try {
                int n = Integer.parseInt(br.readLine());
                System.out.println(kan(n));
            } catch (Exception e) {
                break;
            }
        }
    }
}