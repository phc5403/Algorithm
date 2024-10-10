import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// A / B_1008
public class Main {
    static StringTokenizer st;
    static BufferedReader br;
    static Double A, B;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
//        A = Integer.parseInt(st.nextToken());
//        B = Integer.parseInt(st.nextToken());
//        System.out.println(A / B);
        A = Double.parseDouble(st.nextToken());
        B = Double.parseDouble(st.nextToken());

        System.out.println(A/ B);

    }
}