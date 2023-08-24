climateData <- read.csv("ClimateData.csv")
print(climateData)
print(summary(climateData))

#Printing the data gives us all the raw numbers in the csv file
#Printing the summary of the data gives us central tendency and measure of data dispersion 

#FG represents the number of foggy days
#Empty values are represnted by NA's

print(sum(is.na(climateData)))
#31 empty values

print(class(climateData))
#data frame: data structure that orgnizes data in rows and columns 

print(which(duplicated(climateData)))
climateData <- climateData[-c(19,33,67),] 

print(column_stats <- apply(climateData, 2, function(x) c(mean = mean(x), median = median(x))))
# Mean is 1985.627, median is 1986.000

sapply(climateData[c('T')], sd)
# NA is the result because all the values in the T column are empty
sapply(climateData[c('T')], sd, na.rm = TRUE)                     
# Standard Deviation is 5.450711

pie(
  data <- c(5.54, 16.61, 14.47, 2.8, 15.64, 13.09, 11.42, 16.96, 3.48), 
  labels = c("1940-1949","1950-1959","1960-1969","1970-1979","1980-1989","1990-1999","2000-2009","2010-2019"), 
  main = "Precipitation by Decade Data", 
  col = c("orange", "yellow", "black", "white","blue", "purple", "green", "red", "brown")
)

                            
extreme <- rowSums(climateData[, c("SN", "TN", "TS", "GR")])
print(extreme)
                            
temp1 = min(extreme)
print(temp1)
temp2 = max(extreme)
print(temp2)
boxplot(extreme, ylim = c(0,60), main = "Extreme Weather",ylab="Days")
text(x= 1, y= 51, labels= 2022)
text(x= 1, y= 5, labels= 1948) 
#13-14 has the highest frequency 
hist(climateData$"V", main= "Average Annual Wind Speeds", xlab = "Frequency", ylab="Speed")



num_colors <- 76
color_palette <- colorRampPalette(c("lightblue", "darkblue"))(num_colors)
barplot(climateData$"RA", xlab ="Years", col = color_palette, main = "Years vs. Rainy Days")

max <- rowSums(climateData[c("TM")])
plot(climateData$"TM", xlab ="1948-2011", main = "Years vs. Average Annual Maximum Temperature", ylab= "Rainy Days", xaxt = "n")

