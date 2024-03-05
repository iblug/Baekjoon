import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            String s = br.readLine();
            if (s.length() < 6 || s.length() > 9) {
                sb.append("no\n");
            } else {
                sb.append("yes\n");
            }
        }
        System.out.println(sb);
    }
}