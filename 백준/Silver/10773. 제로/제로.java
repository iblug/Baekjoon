import java.io.IOException;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        Stack<Integer> s = new Stack<>();
        int n = readInt();
        while (n-- > 0) {
            int a = readInt();
            if (a == 0) {
                s.pop();
                continue;
            }
            s.push(a);
        }

        int sum = 0;
        for (int i : s) {
            sum += i;
        }
        System.out.println(sum);
    }

    private static int readInt() throws IOException {
        int value = 0;
        byte v;
        while ((v = read()) <= ' ') ;
        do {
            value = value * 10 + v - '0';
        } while ((v = read()) >= '0' && v <= '9');
        return value;
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
}
