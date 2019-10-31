OneBitGenerator <- function(v, q) {
  t <- runif(1)
  if(t<q){v <- abs(v-1)
  v}
  else v
}

InvertOneBit <- function(v) {
  v <- abs(v-1)
}

a <- c(0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1)

b <- rep_len(0, 52)

for(i in 1:52){b[i] <- OneBitGenerator(a[i], 0.5)}

b <- c(1,0,0,1,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,1,0,1,1,0,1,1,1,0,1,1,0,1,0,1,1,1)

e <- rep_len(0, 52)

for(i in 1:52){
  if(i < 7){e[i] <- OneBitGenerator(a[i], 0.2)}
  else if (i < 14){e[i] <- OneBitGenerator(a[i], 0.1)}
  else if(i < 20){e[i] <- OneBitGenerator(a[i], 0.2)}
  else if(i < 27){e[i] <- OneBitGenerator(a[i], 0.1)}
  else if(i < 33){e[i] <- OneBitGenerator(a[i], 0.2)}
  else if(i < 40){e[i] <- OneBitGenerator(a[i], 0.1)}
  else if(i < 46){e[i] <- OneBitGenerator(a[i], 0.2)}
  else {e[i] <- OneBitGenerator(a[i], 0.25)}
}

c <- matrix(nrow=48, ncol=5)

for(i in 1:48){
  c[i,] <- c(b[i], b[i+1], b[i+2], b[i+3], b[i+4])
}

f <- matrix(nrow=48, ncol=5)

for(i in 1:48){
  f[i,] <- c(e[i], e[i+1], e[i+2], e[i+3], e[i+4])
}

d <- rep_len(0, 48)

for(i in 1:48){
  if(sum(c[i,]) > 2){d[i] <- 1}
}

g <- rep_len(0, 48)

for(i in 1:48){
  if(sum(f[i,]) > 2){g[i] <- 1}
}

# A list containing 13*30 future measurements.

FutureMeasurements <- rep_len(0, 390)

for(i in 2:390){
  if (i%%13 != 0) {FutureMeasurements[i] <- FutureMeasurements[i-1]}
  else FutureMeasurements[i] <- InvertOneBit(FutureMeasurements[i])
}
