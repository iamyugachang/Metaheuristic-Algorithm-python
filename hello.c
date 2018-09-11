#include <stdio.h>
#include <stdlib.h>

int main(){
    int num = 0;
    printf("hello 哈囉 !\n");


    
    
    char command[50];

   strcpy( command, "ls -l" );
   system(command);
    return 0;
}