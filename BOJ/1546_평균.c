# include <stdio.h>
int max_finder(int* array,int Size){
    int max = array[1];
    for (int i = 1;i <= Size-1;i++){
        if (array[i]<array[i+1]){
            max = array[i+1];

        }
    }

    return max;

}

double scam_mean(int* array, int Size,int max){

    double scam_score[Size];
    double scam_sum=0;
    
    for (int i=1; i<Size; i++){
        scam_score[i] = array[i]/max*100;
        scam_sum += scam_score[i];
    }
    double mean= scam_sum/ Size;
    return mean;
}


int main(){
    int size;
    scanf("%d",&size);
    int subject_score[size];

    
    for (int i = 1;i <= size;i++){
        scanf("%d", &subject_score[i]);
    }

    int max = max_finder(subject_score, size);
    double scam = scam_mean(subject_score, size, max);

    printf("%f",scam);
}
