import wordcloud
import matplotlib.pyplot as plt 
import csv

file_ob = open("sample.csv")

reader_ob = csv.reader(file_ob)

reader_contents = list(reader_ob)
print (reader_contents)
text = ""

for row in reader_contents:
	for word in row:
		text+=" "+word
wordcloud = wordcloud.WordCloud(width=480, height=480, background_color="pink").generate(text) 
  
# plot the WordCloud image  
plt.figure() 
plt.imshow(wordcloud, interpolation="bilinear") 
plt.axis("off") 
plt.margins(x=0, y=0) 
plt.show()