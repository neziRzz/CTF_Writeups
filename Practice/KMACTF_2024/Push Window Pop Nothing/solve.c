#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>


uint32_t dword_7FF7B5FD5880[256];
int counter = 0;
char base64_char_before_tranformation = 0;


uint32_t char_to_case(char c) {
    switch (c) {
    case '+': case '2': case 'H': case 'R': case 'X': case 'Z':
    case 'a': case 'l': case 'm': case 'o': case 's': case 'v': case 'x':
        return 0xC000001D;
    case '0': case '6': case '7': case 'A': case 'B': case 'K': case 'L':
    case 'O': case 'T': case 'b': case 'g': case 'y': case 'z':
        return 0xC0000005;
    case '1': case '4': case '5': case '8': case '=': case 'I': case 'J':
    case 'U': case 'W': case 'd': case 'f': case 'r': case 'u':
        return 0xC0000096;
    case '3': case '9': case 'E': case 'G': case 'M': case 'Q': case 'S':
    case 'V': case 'Y': case 'e': case 'h': case 'i': case 'n':
        return 0xC0000094;
    case '/': case 'C': case 'D': case 'F': case 'N': case 'P': case 'c':
    case 'j': case 'k': case 'p': case 'q': case 't': case 'w':
        return 0x80000003;
    default:
        return 0xFFFFFFFF;
    }
}

void transform_char(char* c, uint32_t error_code) {
    base64_char_before_tranformation = *c;

    switch (error_code) {
    case 0x80000003:
        for (int i = 0; i < 0xA; ++i) {
            *c = 7 * (i ^ base64_char_before_tranformation)
                + ((i + 0x33) ^ (*c + 0x45));
        }
        break;
    case 0xC0000005:
        for (int j = 0; j < 0xA; ++j) {
            *c = (*c + j + 0x55) ^ 7;
        }
        break;
    case 0xC000001D:
        for (int k = 0; k < 0xA; ++k) {
            *c = (*c << (k % 3)) & 0x4F
                ^ (0x5B * ((k + base64_char_before_tranformation) ^ *c)
                    + k
                    + (base64_char_before_tranformation >> (((k >> 0x1F) ^ (k & 1)) - (k >> 0x1F))));
        }
        break;
    case 0xC0000094:
        for (int m = 0; m < 0xA; ++m) {
            *c = (m ^ base64_char_before_tranformation) + 0x5D
                * ((m + base64_char_before_tranformation)
                    ^ (3 * base64_char_before_tranformation
                        + m
                        + *c
                        + 4 * m));
        }
        break;
    case 0xC0000096:
        for (int n = 0; n < 0xA; ++n) {
            *c = (0x4D
                * ((7 * n)
                    ^ (*c
                        + (base64_char_before_tranformation << (n % 3))
                        + 0x2D))
                + n
                + base64_char_before_tranformation)
                % 0xFF;
        }
        break;
    }
}


unsigned char dest[] = {
    0x72, 0xBB, 0xB2, 0xCD, 0x58, 0xB2, 0x81, 0x0E, 0xA4, 0xB1, 0xED, 0xDB, 0x84, 0xB2, 0xC0, 0xAA,
    0x60, 0xD0, 0xE8, 0xE8, 0xB0, 0x12, 0x81, 0x1E, 0xED, 0xD0, 0xF3, 0x05, 0xB0, 0xB1, 0x04, 0x04,
    0x7D, 0xF3, 0xC0, 0xE8, 0xED, 0x12, 0xF3, 0xC2, 0x7D, 0x0E, 0x0E, 0x0E, 0x7D, 0x04, 0xC0, 0xBB,
    0xED, 0xB1, 0x81, 0xED, 0xA4, 0xCF, 0xC0, 0x68, 0x84, 0xD0, 0xE2, 0x1B, 0xC2, 0x58, 0x30, 0x30,
    0x00
};
const int dest_length = sizeof(dest) - 1;

unsigned int expected_codes[] = {
    0xC0000094, 0xC0000005, 0xC0000096, 0xC0000005, 0xC0000094, 0xC0000096, 0xC000001D, 0xC0000094,
    0xC0000094, 0xC000001D, 0xC0000094, 0xC000001D, 0xC0000096, 0xC0000096, 0xC0000094, 0x80000003,
    0xC0000094, 0xC0000096, 0xC0000096, 0xC0000096, 0xC000001D, 0xC0000094, 0xC000001D, 0x80000003,
    0xC0000005, 0xC0000096, 0xC0000094, 0xC0000005, 0xC000001D, 0xC000001D, 0x80000003, 0xC0000005,
    0xC000001D, 0xC0000094, 0xC0000094, 0xC0000096, 0xC0000005, 0xC0000094, 0xC0000094, 0xC0000096,
    0xC000001D, 0xC0000094, 0xC000001D, 0xC000001D, 0xC000001D, 0x80000003, 0xC0000094, 0xC0000005,
    0xC0000005, 0xC000001D, 0xC000001D, 0xC0000094, 0xC0000094, 0xC0000005, 0xC0000094, 0xC000001D,
    0xC0000096, 0xC0000096, 0xC0000005, 0x80000003, 0xC0000096, 0xC0000094, 0xC0000096, 0xC0000096
};
const int expected_codes_length = sizeof(expected_codes) / sizeof(expected_codes[0]);


const char* code_to_chars[] = {
    /* 0x80000003 */ "/CDEFNPcjkpqtw",
    /* 0xC0000005 */ "067ABKLOTbgyz",
    /* 0xC000001D */ "+2HRXZalmosvx",
    /* 0xC0000094 */ "39EGMQSVYehin",
    /* 0xC0000096 */ "1458=IJUWdfru"
};

const char* get_chars_for_code(uint32_t code) {
    switch (code) {
    case 0x80000003: return code_to_chars[0];
    case 0xC0000005: return code_to_chars[1];
    case 0xC000001D: return code_to_chars[2];
    case 0xC0000094: return code_to_chars[3];
    case 0xC0000096: return code_to_chars[4];
    default: return "";
    }
}

bool find_matching_string() {
    char solution[expected_codes_length + 1] = { 0 };

    for (int pos = 0; pos < expected_codes_length; pos++) {
        const char* valid_chars = get_chars_for_code(expected_codes[pos]);
        int valid_chars_len = strlen(valid_chars);
        bool found = false;

        for (int i = 0; i < valid_chars_len; i++) {

            char test_char = valid_chars[i];
            char transformed_char = test_char;
            transform_char(&transformed_char, expected_codes[pos]);

            if ((unsigned char)transformed_char == dest[pos]) {
                solution[pos] = test_char;
                found = true;
                printf("Found char %d: %c (-> 0x%02X)\n", pos, test_char, (unsigned char)transformed_char);
                break;
            }
        }

        if (!found) {
            printf("Failed to find matching char at position %d\n", pos);
            return false;
        }
    }

    solution[expected_codes_length] = '\0';
    printf("\nFinal solution: %s\n", solution);


    char verify[expected_codes_length + 1];
    strcpy(verify, solution);
    for (int i = 0; i < expected_codes_length; i++) {
        transform_char(&verify[i], expected_codes[i]);
    }

    if (memcmp(verify, dest, expected_codes_length) == 0) {
        printf("Verification successful!\n");
    }
    else {
        printf("Verification failed!\n");
    }

    return true;
}

int main() {
    if (expected_codes_length != dest_length) {
        printf("Error: expected_codes length (%d) doesn't match dest length (%d)\n",
            expected_codes_length, dest_length);
        return 1;
    }

    clock_t start = clock();

    if (!find_matching_string()) {
        printf("Failed to find solution\n");
    }

    clock_t end = clock();
    double elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Time elapsed: %.2f seconds\n", elapsed);

    return 0;
}
