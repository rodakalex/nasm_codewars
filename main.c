#include <inttypes.h>
#include <stdio.h>
#include <stdint.h>
#include <malloc.h>


extern char *get_age(const char *current);


int main(void) {
    printf("%d need 5\n", get_age("4 years old"));
    printf("%d need 9\n", get_age("9 years old"));
    return 0;
}
