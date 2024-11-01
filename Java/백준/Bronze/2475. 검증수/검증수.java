//import java.io.BufferedReader;
//import java.util.StringTokenizer;
//
//public class Main {
//    public static BufferedReader br;
//    public static StringTokenizer st;
//    public static void main(String[] args) {
//
//    }
//}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 검증수_2475
public class Main {
    static StringTokenizer st;
    static BufferedReader br;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());

        double res = 0;
        for(int i=0; i < 5; i++) {
            double num = Double.parseDouble(st.nextToken());
            res += Math.pow(num, 2);
        }

        System.out.println((int)res % 10);
    }
}
