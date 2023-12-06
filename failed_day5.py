from itertools import batched
import utils

quiz = utils.read_quiz(5, is_example=False)


type match_dict = dict[tuple[int, int], tuple[int, int]]
type resource_maps = dict[str, match_dict]

maps_dict: resource_maps = {
    "seed-to-soil": {},
    "soil-to-fertilizer": {},
    "fertilizer-to-water": {},
    "water-to-light": {},
    "light-to-temperature": {},
    "temperature-to-humidity": {},
    "humidity-to-location": {},
}


def create_matchdict(destination: int, source: int, number: int) -> match_dict:
    return {(destination, destination + number - 1): (source, source + number - 1)}


def source_to_destination(source: int, matching: match_dict) -> int:
    for dest_tuple, source_tuple in matching.items():
        min_destination, _ = dest_tuple
        min_source, max_source = source_tuple
        if min_source <= source <= max_source:
            return min_destination + (source - min_source)
    return source


def find_destination(seed: int, re_maps: resource_maps = maps_dict) -> int:
    soil = source_to_destination(seed, re_maps["seed-to-soil"])
    fertilizer = source_to_destination(soil, re_maps["soil-to-fertilizer"])
    water = source_to_destination(fertilizer, re_maps["fertilizer-to-water"])
    light = source_to_destination(water, re_maps["water-to-light"])
    temperature = source_to_destination(light, re_maps["light-to-temperature"])
    humidity = source_to_destination(temperature, re_maps["temperature-to-humidity"])
    location = source_to_destination(humidity, re_maps["humidity-to-location"])
    return location


for line in quiz:
    match line.strip().split():
        case []:
            continue
        case ["seeds:", *args]:
            seeds_1 = [*map(int, args)]
        case [maps, "map:"]:
            now_map = maps
        case [dest, source, num]:
            maps_dict[now_map] |= create_matchdict(
                destination=int(dest), source=int(source), number=int(num)
            )
        case _:
            raise Exception("Should Not be here")

# Part 1
# print(min([*map(find_destination, seeds_1)]))
# Part 2
min_des = 100000000000000000
# seed_ranges = [range(start, start + length) for start, length in batched(seeds_1, 2)]

