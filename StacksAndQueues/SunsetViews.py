def sunsetViews(buildings, direction):
	building_stacks = []
	if direction == "EAST":
		for i in range(len(buildings) - 1, -1, -1):
			if len(building_stacks) == 0:
				building_stacks.append(i)
			else:
				if buildings[building_stacks[-1]] < buildings[i]:
					building_stacks.append(i)
		building_stacks.reverse()
	else:
		for i in range(len(buildings)):
			if len(building_stacks) == 0:
				building_stacks.append(i)
			else:
				if buildings[building_stacks[-1]] < buildings[i]:
					building_stacks.append(i)
    return building_stacks
