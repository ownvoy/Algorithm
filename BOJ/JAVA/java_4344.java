import java.util.Scanner;

public class java_4344 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int test_number = input.nextInt(); // 첫번째 숫자

        int[] test_number_array = new int[test_number]; // 각 줄의 첫번째 숫자

        for (int i = 0; i < test_number; i++) {
            test_number_array[i] = input.nextInt();
            // 배열초기화해야되는지 확인
            int[] test_case = new int[test_number_array[i]];
            int sum = 0;

            for (int j = 0; j < test_case.length; j++) {
                test_case[j] = input.nextInt();
                sum += test_case[j];

            }
            int mean = sum / test_case.length;
            float greatermean = 0;
            for (int j = 0; j < test_case.length; j++) {
                if (test_case[j] > mean) {
                    greatermean += 1;
                }
            }

            float gradeA = greatermean / test_case.length;
            System.out.printf("%.3f%%\n", gradeA * 100);

        }

    }

}
