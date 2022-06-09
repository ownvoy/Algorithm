import java.util.Scanner;

public class java_11720 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int number = input.nextInt();
        String str = input.next();
        char[] ch = str.toCharArray();
        int[] numarray = new int[number];
        int sum = 0;
        for (int i = 0; i < ch.length; i++) {
            numarray[i] = (int) ch[i] - 48;
            sum += numarray[i];

        }
        System.out.printf("%d", sum);
    }
}
