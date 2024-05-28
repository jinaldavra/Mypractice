#include <stdio.h>

int main() {
    
    float score[5] = {50, 60, 70, 80, 90};
    
    int total = 0;                                               // Single Dimensional Array
    for(int marks = 1; marks <= 5; marks++){
        printf("sub-%d : marks - %.2f\n", marks, score[marks-1]);
        total += score[marks-1];
    }
    
    printf("Percentage : %f", total/500);
    return 0;
}


#include <stdio.h>

 int main() {
    
     int matrix1[2][3] = {
         {10,20,30},
         {40,50,60}
     };
     int matrix2[2][3] = {
         {1,1,1},
         {1,1,1}
     };                                                            // Multi Dimensional Array
    
     for(int row = 0; row<=1; row++){
         for(int col = 0; col<=2; col++){
             printf("%d ", matrix1[row][col] * matrix2[row][col]);
         }
         printf("\n");
     }
     return 0;
 }


#include <stdio.h>

int main() {
    int num[5] = {55,66,77,88,99};  
  
    for (int i = 0; i < 5; i++) {
        // Soft delete
        if (num[i] == 88){
            continue;
        }
        printf("Element at index %d: %d\n", i, num[i]);            // Delete Array   
    }

    return 0;
}


#include <stdio.h>

int main() {
    int num[5] = {81,82,86,84,85};  
    num[2] = 83;  
    for (int i = 0; i < 5; i++) {
        printf("Element at index %d: %d\n", i, num[i]);             // Update Array 
    }

    return 0;
}


#include <stdio.h>

int main() {
    int num[5] = {81,82,83,84,85};  
    num[5] = 86;  
    for (int i = 0; i < 6; i++) {
        printf("Element at index %d: %d\n", i, num[i]);             // Add new index
    }

    return 0;
}


#include<stdio.h>
int main(){
    float marks[5] = {23,34,45,56,67};
    const char *sub[5] = {"CSS","Java","Python","C++","Html"};
    
    for(int i = 0; i < 5; i++){
        float score;
        printf("%s mark : ",sub[i]);
        scanf("%f",&score);
        marks[i] = score;                                         // sub via marks
    }
    int total = 0;
    for(int i = 0; i < 5; i++){
        printf("%s mark : %2.f\n",sub[i],marks[i]);
        total += marks[i];
    }
    printf("Total : %d\n",total);
    printf("Percentage : %2.f",total/500);
}

