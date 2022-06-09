import java.util.Scanner;

public class java_10809 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String str = input.nextLine();
        char[] cr = str.toCharArray();
        int[] count = new int[26];

        // 배열초기화
        for (int h = 0; h < count.length; h++) {
            count[h] = -1;
        }

        for (int i = 0; i < cr.length; i++) {
            int ascii = (int) cr[i];
            for (int j = 97; j <= 122; j++) {
                if (count[j - 97] == -1) {
                    if (ascii == j) {
                        count[j - 97] = i;
                    }
                }
            }
        }

        for (int p = 0; p < count.length; p++) {
            System.out.printf("%d ", count[p]);
        }
    }
}
