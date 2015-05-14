# ಕಸಿ
------

ಕನ್ನಡದಲ್ಲಿ 'ಸಿ'

## Usage:
=========

```bash
bash-4.2:src/$ make
rm -f fact.kasi.C fact.kasi.o fact
BEFORE TRANSFORM
***************************
#include <stdio.h>

ಪೂರ್ಣಸಂಖ್ಯೆ main(ಪೂರ್ಣಸಂಖ್ಯೆ argc, ಅಕ್ಷರ *argv[]) {
	ಪೂರ್ಣಸಂಖ್ಯೆ number, index, result = 1;
	printf("Enter the number:");
	scanf("%d", &number);
	ಸಲುವಾಗಿ(index = 1; index <= number; result *= index++);
	printf("Factorial of %d is %d\n", number, result);
	ಕಳುಹಿಸು 0;
}
***************************

AFTER TRANSFORM
***************************
#include <stdio.h>

int main(int argc, char *argv[]) {
	int number, index, result = 1;
	printf("Enter the number:");
	scanf("%d", &number);
	for(index = 1; index <= number; result *= index++);
	printf("Factorial of %d is %d\n", number, result);
	return 0;
}
***************************

COMPILE
***************************
gcc -c -Wall fact.kasi.C
***************************

LINK
***************************
gcc fact.kasi.o -o fact
***************************

echo 3 | ./fact
Enter the number:Factorial of 3 is 6

***************************
*****BUILD SUCCESSFULL*****
***************************
```
