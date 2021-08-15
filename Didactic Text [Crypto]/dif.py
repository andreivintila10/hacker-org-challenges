original = []
with open('original.txt','r') as f:
  for line in f:
    for word in line.split():
      word = word.replace(".", "");
      word = word.replace(",", "");
      original.append(word);

modified = []
with open('modified.txt','r') as f:
  for line in f:
    for word in line.split():
      word = word.replace(".", "");
      word = word.replace(",", "");
      modified.append(word);

original_len = len(original);
modified_len = len(modified);

index1 = index2 = 0;
while (index1 < original_len and index2 < modified_len):
	if (original[index1] != modified[index2]):
		print(modified[index2]);
		index2 += 1
	else:
	  index1 += 1
	  index2 += 1
