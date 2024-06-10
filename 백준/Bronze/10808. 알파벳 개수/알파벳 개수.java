import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        int[] a = new int[26];
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        for (int i = 0; i < s.length(); i++) {
            a[s.charAt(i)-'a']++;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 26; i++) {
            sb.append(a[i]).append(' ');
        }

        System.out.println(sb);
    }
}