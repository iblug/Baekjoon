import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int cnt = 1;
        Deque<Integer> stk = new ArrayDeque<>();
        boolean flag = true;
        int current = readInt();
        while (cnt <= n && current != 0) {
            if (current == cnt) {
                cnt++;
                current = readInt();
            } else if (stk.isEmpty()) {
                stk.push(current);
                current = readInt();
            } else if (stk.peek() == cnt) {
                stk.pop();
                cnt++;
            } else if (stk.peek() < current) {
                flag = false;
                break;
            } else {
                stk.push(current);
                current = readInt();
            }
        }
        System.out.println(flag ? "Nice" : "Sad");
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
