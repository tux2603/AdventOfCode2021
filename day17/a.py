import re
from numba import njit, prange, int32, int64, boolean
import numpy as np

@njit()
def path_generator(vel_x: int64, vel_y: int64) -> int64[:]:
    x, y = 0, 0
    while True:
        yield (x, y)
        x += vel_x
        y += vel_y

        if vel_x > 0:
            vel_x -= 1
        elif vel_x < 0:
            vel_x += 1
        vel_y -= 1

@njit(parallel=True, cache=True)
def get_max_y(target: int32[:]):
    t_min_x = target[0]
    t_max_x = target[1]
    t_min_y = target[2]
    t_max_y = target[3]
    search_size = 20000

    max_y_candidates = np.zeros(search_size**2, dtype=np.int64)

    for vel_x in prange(search_size):
        for vel_y in prange(search_size):
            p = path_generator(vel_x, vel_y)

            passed_x = False
            passed_y = False
            local_max_y = 0

            for x, y in p:
                if y > local_max_y:
                    local_max_y = y

                if passed_x or passed_y:
                    break

                if y > t_max_y:
                    continue

                if y < t_min_y:
                    passed_y = True
                    continue

                if x < t_min_x:
                    continue

                if x > t_max_x:
                    passed_x = True
                    continue

                max_y_candidates[vel_x + vel_y * 2000] = local_max_y
                break

    print("candidates found")
    return max(max_y_candidates)

# corrds in the format x/y=min..max
# Parse out the x coords of the targer
with open('input') as f:
    line = f.readline()
    x_min, x_max = sorted(map(int, re.findall(r'x=(-?\d+)..(-?\d+)', line)[0]))
    y_min, y_max = sorted(map(int, re.findall(r'y=(-?\d+)..(-?\d+)', line)[0]))



print(get_max_y((x_min, x_max, y_min, y_max)))

