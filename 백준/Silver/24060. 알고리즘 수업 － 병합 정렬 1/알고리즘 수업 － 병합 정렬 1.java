import java.io.IOException;

public class Main {
    static int[] tmp;
    static int cnt, ans, k;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        cnt = 0;
        ans = -1;
        k = readInt();
        int[] a = new int[n];
        tmp = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = readInt();
        }

        merge_sort(a, 0, n-1);
        System.out.println(ans);
    }

    static void merge_sort(int[] a, int p, int r) {
        if (p < r) {
            int q = (p + r) / 2;
            merge_sort(a, p, q);
            merge_sort(a, q + 1, r);
            merge(a, p, q, r);
        }
    }

    static void merge(int[] a, int p, int q, int r) {
        int i = p, j = q + 1, t = 0;
        while (i <= q && j <= r) {
            if (a[i] <= a[j]) {
                tmp[t++] = a[i++];
            } else {
                tmp[t++] = a[j++];
            }
        }
        while (i <= q) {
            tmp[t++] = a[i++];
        }
        while (j <= r) {
            tmp[t++] = a[j++];
        }
        i = p;
        t = 0;
        while (i <= r) {
            cnt++;
            if (cnt == k) {
                ans = tmp[t];
            }
            a[i++] = tmp[t++];
        }
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