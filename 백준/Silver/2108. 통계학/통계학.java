import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        int n = readInt();
        int sum = 0, min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        List<Integer> list = new ArrayList<>();
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int num = readInt();
            sum += num;
            if (num < min) {
                min = num;
            }
            if (num > max) {
                max = num;
            }
            list.add(num);
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        Collections.sort(list);

        int maxFreq = Collections.max(map.values());
        List<Integer> freqList = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getValue() == maxFreq) {
                freqList.add(entry.getKey());
            }
        }
        Collections.sort(freqList);


        StringBuilder sb = new StringBuilder();
        sb.append(Math.round((float) sum/n)).append("\n");
        sb.append(list.get(n/2)).append("\n");
        sb.append(freqList.size() > 1 ? freqList.get(1) : freqList.get(0)).append("\n");
        sb.append(max - min);

        System.out.println(sb);
    }

    private static int readInt() throws IOException {
        int t = 0;
        byte v;
        while ((v = read()) <= 32);
        boolean negative = (v == '-');
        if (negative) v = read();
        do {
            t = t * 10 + (v - '0');
        } while ((v = read()) >= '0' && v <= '9');
        return (negative) ? -t : t;
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