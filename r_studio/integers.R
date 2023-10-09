# Method 1
for (i in 1:10) {
  print(i)
}

# Method 2
print(1:10)

# Method 3
for (i in c(1:10)) {
  print(i)
}

# Method 4 #code wont work as it prints finite 10s
while (i<= 10) {
print(i)
}

# Method 5
for (i in c(1:10)){
  cat(i,"")
}

# Method 6
cat(1:10)
