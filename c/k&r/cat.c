#include <stdlib.h>
#include <stdio.h>

// cat: concatenate files, version 2
int main (int argc, char *argv[]) {
    FILE *fp;
    void filecopy(FILE *, FILE *);
    char *name = argv[0];

    // If no arguments were passed in
    if (argc == 1) {
        filecopy(stdin, stdout);
    } else {
        for (; argc > 1; argc--, argv++) {
            fp = fopen(*argv, "r");
            if (fp == NULL) {
                fprintf(stderr, "%s: can't open %s\n", name, *argv);
                exit(EXIT_FAILURE);
            } else {
                filecopy(fp, stdout);
                fclose(fp);
            }
        }
    }

    if (ferror(stdout)) {
        fprintf(stderr, "%s: error writing stdout\n", name);
        exit(2);
    }

    exit(0);
}
