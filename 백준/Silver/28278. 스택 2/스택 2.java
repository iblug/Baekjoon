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
                    sb.append(s.isEmpty() ? "-1" : s.pop()).append("\n");
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

    private static int readInt() throws IOException {
        int t = 0;
        byte v;
        while ((v = read()) <= 32);
        do t = (t << 3) + (t << 1) + (v & 15);
        while (isNumber(v = read()));
        return t;
    }

    static final int SIZE = 1 << 13;
    static byte[] buffer = new byte[SIZE];
    static int index, size;
    private static byte read() throws IOException {
        if (index == size) {
            size = System.in.read(buffer, index = 0, SIZE);
            if (size < 0) buffer[0] = -1;
        }
        return buffer[index++];
    }

    static boolean isNumber(byte c) {
        return 47 < c && c < 58;
    }
}