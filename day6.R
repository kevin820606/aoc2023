library(tidyverse)
time <- c(7, 15, 30)
distance <- c(9, 40, 200)

time <- c(41, 96, 88, 94)
distance <- c(214, 1789, 1127, 1055)

calc_dist <- function(time, dist) {
    sum(
        ((log(0:time) + log(rev(0:time)))) > log(dist)
    )
}
print(mapply(calc_dist, time, distance))
print(calc_dist(
    as.numeric(paste0(time, collapse = "")),
    as.numeric(paste0(distance, collapse = ""))
))
