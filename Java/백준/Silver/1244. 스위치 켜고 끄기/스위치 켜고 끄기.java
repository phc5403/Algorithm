import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
	static int size;
	static boolean[] lst;
	static int N;
	static int gender;
	static int num;
	
	public static void main(String[] args) throws IOException {	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		size = Integer.parseInt(st.nextToken());
		lst = new boolean[size];
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < size; i++) {
			if (Integer.parseInt(st.nextToken()) == 1) {
				lst[i] = true;
			} else {
				lst[i] = false;
			}
		}
		
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			gender = Integer.parseInt(st.nextToken());
			num = Integer.parseInt(st.nextToken());
			
			 func(gender, num);
		}
		for (int i = 0; i < size; i++) {
			if (i != 0 && i % 20 == 0) {
				System.out.println();
			}
			
			if (lst[i] == true) {
				System.out.print("1");
				if (i != size - 1) System.out.print(" ");
			} else {
				System.out.print("0");
				if (i != size - 1) System.out.print(" ");
			}
		}
	}
	
	static boolean[] func(int gender, int num) {
		if (gender == 1) { // 남
			for (int i = 0; i < size; i++) {
				if ((i + 1) % num == 0) {  // 스위치 번호가 자기가 받은 수의 배수
					lst[i] = !lst[i];
				}
			}
//			System.out.println("남");
//			System.out.println(Arrays.toString(lst));
			return lst;
			
		} else {  // 여
			boolean cur = lst[num - 1];
			int left = num - 2;
			int right = num;
			
			lst[num - 1] = !lst[num - 1];
			while (true) {
				if ((0 <= left && right < size) && (lst[left] == lst[right])) {
					lst[left] = !lst[left];
					lst[right] = !lst[right];
					left--;
					right++;
				} else {
					break;
				}
			}
//			System.out.println("여");
//			System.out.println(Arrays.toString(lst));
			return lst;
		}
	}
}

