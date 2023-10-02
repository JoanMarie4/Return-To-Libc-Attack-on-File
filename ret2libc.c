#include <stdio.h>
#include <string.h>

void unused_fn1(){
  asm volatile ("pop %%rdi\n\t"
      "ret"
      :
      :
      : "rdi");
}

void unused_fn2(){
  asm volatile ("push %%rdi\n\t"
      "ret"
      :
      :
      : "rdi");
}

int main(){
    FILE *fp;
    char noun[20];
    fp = fopen("pizza.txt", "w");
    fputs("The secret ingredient to John's pizza is... ", fp);
    fclose(fp);

    puts("Hello, please type a noun: ");
    gets(noun);
    fp = fopen("pizza.txt", "a");
    fputs(noun, fp);
    fputs("!\n", fp);
    fclose(fp);
    printf("Madlibs written to file pizza.txt\n");
}


