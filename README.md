# ಕಸಿ
------

ಕನ್ನಡದಲ್ಲಿ 'ಸಿ'

## Usage:
=========

```bash
bash-4.2:src $ cat fact.kasi && ./kasi.py fact.kasi && cat fact.kasi.C && gcc -Wall fact.kasi.C -o fact && (echo 3 | ./fact) 
#include <stdio.h>

ಪೂರ್ಣಸಂಖ್ಯೆ main(ಪೂರ್ಣಸಂಖ್ಯೆ argc, ಅಕ್ಷರ *argv[]) {
	ಪೂರ್ಣಸಂಖ್ಯೆ number, index, result = 1;
	printf("Enter the number:");
	scanf("%d", &number);
	ಸಲುವಾಗಿ(index = 1; index <= number; result *= index++);
	printf("Factorial of %d is %d\n", number, result);
	ಕಳುಹಿಸು 0;
}
#include <stdio.h>

int main(int argc, char *argv[]) {
	int number, index, result = 1;
	printf("Enter the number:");
	scanf("%d", &number);
	for(index = 1; index <= number; result *= index++);
	printf("Factorial of %d is %d\n", number, result);
	return 0;
}
Enter the number:Factorial of 3 is 6
```
