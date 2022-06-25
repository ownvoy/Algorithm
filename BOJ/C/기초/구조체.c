# include <stdio.h>

typedef struct __student{
    int num;
    int grade;
} student;

int main(){

    printf("3");
    student *s1;
    printf("3");
    scanf("%d", &s1->num);
    scanf("%d", &s1->grade);
    printf("%d\n", s1->num);
    printf("%d\n", ++s1->grade);
}