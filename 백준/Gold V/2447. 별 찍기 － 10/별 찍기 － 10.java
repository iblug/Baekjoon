import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static StringBuilder[] sbArr;
    static void star(int x, int y, int t) {
        t /= 3;
        if (t == 0) {
            return;
        }
        for (int i = x+t; i < x+2*t; i++) {
            for (int j = y+t; j < y+2*t; j++) {
                sbArr[i].setCharAt(j, ' ');
            }
        }
        star(x, y, t);
        star(x, y+t, t);
        star(x, y+2*t, t);
        star(x+t, y, t);
        star(x+t, y+2*t, t);
        star(x+2*t, y, t);
        star(x+2*t, y+t, t);
        star(x+2*t, y+2*t, t);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        sbArr = new StringBuilder[n];
        for (int i = 0; i < n; i++) {
            StringBuilder s = new StringBuilder();
            for (int j = 0; j < n; j++) {
                s.append("*");
            }
            sbArr[i] = s;
        }
        star(0, 0, n);

        for (StringBuilder s : sbArr) {
            sb.append(s).append("\n");
        }
        System.out.println(sb);
    }
}