library(bit64)
time <- c(7, 15, 30)
distance <- c(9, 40, 200)

time <- c(41, 96, 88, 94)
distance <- c(214, 1789, 1127, 1055)

calc_dist <- function(time, dist) {
    sum(
        as.integer64(0):time * rev(as.integer64(0):time) > dist
    )
}
print(mapply(calc_dist, time, distance))
print(calc_dist(
    as.integer64(paste0(time, collapse = "")),
    as.integer64(paste0(distance, collapse = ""))
))
