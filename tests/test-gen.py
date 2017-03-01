from random import uniform, random, choice


idx_num = int(uniform(1,10))
op_num = int(uniform(30,300))

allocated = [False] * idx_num
alloc_sizes = [-1] * idx_num
operations = []
for i in range(op_num):
	idx_list = filter(lambda (idx, val): not val, enumerate(allocated))
	idx_list = [idx for (idx, val) in idx_list]
	if len(idx_list) == 0:
		action = "f"
	elif len(idx_list) == idx_num:
		action = "a"
	else:
		toss = random()
		action = "a" if toss > 0.5 else "f"
	op_line=""
	if action == "a":
		al_idx = choice(idx_list)
		size = int(uniform(2,4099))
		allocated[al_idx] = True
		alloc_sizes[al_idx] = size
		op_line = "a " + str(al_idx) + " " + str(size)
	else:
		alloc_list = filter(lambda (idx, val): val, enumerate(allocated))
		alloc_list = [idx for (idx, val) in alloc_list]
		fr_idx = choice(alloc_list)
		allocated[fr_idx] = False
		alloc_sizes[fr_idx] = -1
		op_line += "f " +  str(fr_idx)
	operations.append(op_line)

while True:
	alloc_list = filter(lambda (idx, val): val, enumerate(allocated))
	alloc_list = [idx for (idx, val) in alloc_list]
	if len(alloc_list) == 0: break
	fr_idx = choice(alloc_list)
	allocated[fr_idx] = False
	alloc_sizes[fr_idx] = -1
	operations.append("f " +  str(fr_idx))

print "20000"
print str(idx_num)
print str(len(operations))
print "1"
for op in operations:
	print op

