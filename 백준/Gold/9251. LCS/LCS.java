import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static String a, b;
    static int[][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        a = br.readLine();
        b = br.readLine();

        dp = new int[b.length()+1][a.length()+1];
        LCS(a, b);
        System.out.println(dp[b.length()][a.length()]);
    }

    private static void LCS(String a, String b) {
        for (int j = 0; j < b.length(); j++) {
            for (int i = 0; i < a.length(); i++) {
                if (a.charAt(i) == b.charAt(j)) {
                    dp[j+1][i+1] = dp[j][i] + 1;
                } else {
                    dp[j+1][i+1] = Math.max(dp[j][i+1], dp[j+1][i]);
                }
            }
        }
    }

}