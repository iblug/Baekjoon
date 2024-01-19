import java.io.IOException;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        Stack<Integer> s = new Stack<>();
        StringBuilder sb = new StringBuilder();
        int n = readInt();
        while (n-- > 0) {
            int a = readInt();
            switch (a) {
                case 1:
                    int b = readInt();
                    s.push(b);
                    break;
                case 2:
                    if (s.isEmpty()) {
                        sb.append("-1\n");
                    } else {
                        sb.append(s.pop()).append("\n");
                    }
                    break;
                case 3:
                    sb.append(s.size()).append("\n");
                    break;
                case 4:
                    sb.append(s.isEmpty() ? "1\n" : "0\n");
                    break;
                case 5:
                    sb.append(s.isEmpty() ? "-1" : s.get(s.size() - 1)).append("\n");
                    break;
                default:
                    break;
            }
        }
        System.out.println(sb);
    }
    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }
        return t;
    }
}