library(ggplot2)

x <- seq(-2 * pi, 2 * pi, length.out = 1000)
y <- sin(x)

ggplot(data.frame(x, y), aes(x, y)) +
  geom_line() +
  ggtitle('sin(x) Function') +
  xlab('x') +
  ylab('sin(x)')

