import math
import utils

quiz = utils.read_quiz(6, False)

# part 1
time = list(map(int, quiz[0].split()[1:]))
dist = list(map(int, quiz[1].split()[1:]))


def get_dist(total_time: int) -> int:
    presstime = 0
    run_dist = []
    for presstime in range(0, (total_time + 1) // 2):
        runtime = total_time - presstime
        speed = presstime
        run_dist.append(speed * runtime)
    return run_dist


def beat_time(time: int, enemy_dist: int) -> int:
    run_dist = get_dist(time)
    return sum(map(lambda x: x > enemy_dist, run_dist)) * 2


answer = math.prod([beat_time(t, ed) for t, ed in zip(time, dist)])
print(answer)

# part 2
time = int("".join(quiz[0].split()[1:]))
dist = int("".join(quiz[1].split()[1:]))
print(beat_time(time, dist))
