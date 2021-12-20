#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#ifndef ITERATIONS
#    define ITERATIONS 2
#endif

void print_grid(uint8_t **grid, int size_x, int size_y) {
    for (int y = 0; y < size_y; y++) {
        for (int x = 0; x < size_x; x++) {
            printf("%c", grid[x][y] == 1 ? '#' : '.');
        }
        printf("\n");
    }
}

int main() {
    uint8_t rules[512];

    // Open a file called input_test for reading
    FILE *file = fopen("input", "r");

    // For the first 512 characters, a '.' corresponds to 0, and a '#' corresponds to 1
    for (int i = 0; i < 512; ++i) {
        char c = fgetc(file);
        if (c == '.') {
            rules[i] = 0;
        } else if (c == '#') {
            rules[i] = 1;
        }
    }

    // The next two ints will be the size of the grid
    int grid_size_x, grid_size_y;
    fscanf(file, "%d %d\n", &grid_size_x, &grid_size_y);

    // Create the grid array
    uint8_t **grid = malloc((grid_size_x + ITERATIONS * 2) * sizeof(uint8_t *));

    for (int x = 0; x < grid_size_x + ITERATIONS * 2; ++x) {
        grid[x] = malloc((grid_size_y + ITERATIONS * 2) * sizeof(uint8_t));

        for (int y = 0; y < grid_size_y + ITERATIONS * 2; ++y) {
            grid[x][y] = 0;
        }
    }

    for (int y = 0; y < grid_size_y; ++y) {
        for (int x = 0; x < grid_size_x; ++x) {
            char c = fgetc(file);
            if (c == '.') {
                grid[x + ITERATIONS][y + ITERATIONS] = 0;
            } else if (c == '#') {
                grid[x + ITERATIONS][y + ITERATIONS] = 1;
            }
        }
        // Discard the new line
        fgetc(file);
    }

    grid_size_x += ITERATIONS * 2;
    grid_size_y += ITERATIONS * 2;

    // printf("Grid size is %lu\n", sizeof(grid[0]));

    // print_grid((uint8_t **)grid, grid_size_x, grid_size_y);

    // If alternating is true, then the neighbors will be inverted for odd numbered iterations and the rule result will be inverted for even numbered iterations
    bool alternating = rules[0] && !rules[1];

    for (int i = 0; i < ITERATIONS; ++i) {
        #pragma omp parallel for
        for (int x = 0; x < grid_size_x; ++x) {
            for (int y = 0; y < grid_size_y; ++y) {
                uint16_t neighbors = 0x0;

                if (x > 0 && y > 0) neighbors |= (grid[x - 1][y - 1] & 0x1) << 8;
                if (y > 0) neighbors |= (grid[x][y - 1] & 0x1) << 7;
                if (x < grid_size_x - 1 && y > 0) neighbors |= (grid[x + 1][y - 1] & 0x1) << 6;
                if (x > 0) neighbors |= (grid[x - 1][y] & 0x1) << 5;
                neighbors |= (grid[x][y] & 0x1) << 4;
                if (x < grid_size_x - 1) neighbors |= (grid[x + 1][y] & 0x1) << 3;
                if (x > 0 && y < grid_size_y - 1) neighbors |= (grid[x - 1][y + 1] & 0x1) << 2;
                if (y < grid_size_y - 1) neighbors |= (grid[x][y + 1] & 0x1) << 1;
                if (x < grid_size_x - 1 && y < grid_size_y - 1) neighbors |= (grid[x + 1][y + 1] & 0x1) << 0;

                if (alternating && i % 2) {
                    neighbors ^= 0x1FF;
                }

                uint8_t rule = rules[neighbors];

                if (alternating && !(i % 2)) {
                    rule ^= 0x1;
                }

                // printf("Cell (%2d, %2d) had %3d neighbors, corresponding entry is %d\n", x, y, neighbors, rule);

                grid[x][y] |= rule << 1;
            }
        }

        // Shift all the cells to the right
        #pragma omp parallel for
        for (int x = 0; x < grid_size_x; ++x) {
            for (int y = 0; y < grid_size_y; ++y) {
                grid[x][y] >>= 1;
            }
        }

        // for (int i = 0; i < grid_size_x; ++i) {
        //     printf("-");
        // }
        // printf("\n");
        // print_grid(grid, grid_size_x, grid_size_y);
    }

    // Find the number of cells that are on
    int on = 0;
    #pragma omp parallel for reduction(+:on)
    for (int x = 0; x < grid_size_x; ++x) {
        for (int y = 0; y < grid_size_y; ++y) {
            on += grid[x][y] & 0x1;
        }
    }

    printf("On: %d\n", on);

    // Free the grid
    for (int i = 0; i < grid_size_x; ++i) {
        free(grid[i]);
    }
    free(grid);
}
