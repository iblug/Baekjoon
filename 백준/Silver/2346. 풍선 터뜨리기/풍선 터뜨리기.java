import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    public static void main(String[] args) throws IOException {
        int n = readInt();
        Deque<Tuple> q = new ArrayDeque<>();
        for (int i = 1; i <= n; i++) {
            q.offerLast(new Tuple(i, readInt()));
        }
        StringBuilder sb = new StringBuilder();
        while (q.size() > 1) {
            Tuple c = q.pollFirst();
            sb.append(c.x).append(" ");
            int r = c.y;
            if (r > 0) {
                while (r-- > 1) {
                    q.offerLast(q.pollFirst());
                }
            } else {
                while (r++ < 0) {
                    q.offerFirst(q.pollLast());
                }
            }
        }
        sb.append(q.peek().x);
        System.out.println(sb);
    }

    static int readInt() throws IOException {
        int v, t = 0;
        boolean isNegative = false;
        while ((v = System.in.read()) > 33) {
            if (v == '-') {
                isNegative = true;
                continue;
            }
            t = t * 10 + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }
        return isNegative ? -t : t;
    }

    static class Tuple {
        int x, y;

        Tuple(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "{" + this.x + ", " + this.y + "}";
        }
    }
}
