import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static int recursion(String s, int l, int r) {
        if (l >= r) return l + 1;
        else if (s.charAt(l) != s.charAt(r)) return -(l + 1);
        else return recursion(s, l + 1, r - 1);
    }

    public static int isPalindrome(String s) {
        return recursion(s, 0, s.length() - 1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        while (t-- > 0) {
            String s = br.readLine();
            int p = isPalindrome(s);
            if (p <= 0) {
                sb.append("0 ").append(-p);
            } else {
                sb.append("1 ").append(p);
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }
}