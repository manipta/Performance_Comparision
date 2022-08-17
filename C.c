#include<stdio.h>
#include<ctype.h>
int main()
{
      FILE *fp1;
      char ch;
      double count=0;
      fp1 = fopen("my_file.txt", "r");
      while((ch=fgetc(fp1))!=EOF)
      {
            count=count+1;
      } 
      printf("%d",count);
      fclose(fp1);
      return 0;
}
