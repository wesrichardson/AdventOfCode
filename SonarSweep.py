import AdventUtils

def depth_changes(depth_list):
    print("Part 1 - Find the increases in depths")
    increases = 0
    decreases = 0
    same = 0
    currentDepth = 0
    for idx, val in enumerate(depth_list):
        if (idx != 0):
            if (val > currentDepth):
                #print("{} (increased)".format(val))
                increases += 1
            elif (val < currentDepth):
                #print("{} (decreased)".format(val))
                decreases += 1
            else:
                same += 1
        currentDepth = val

    print("Results:")
    print("Increases: [{}] \nDecreases: [{}] \nSame Depth: [{}]\n".format(increases, decreases, same))

def sliding_window(depths):
    print("Part 2 - Find the sliding data increases")
    starting_index = 0
    loop = True
    increase = 0
    decrease = 0
    same = 0
    current = 0
    while(loop):
        try:
            var1=int(depths[starting_index])
            var2=int(depths[starting_index+1])
            var3=int(depths[starting_index+2])
            total = var1+var2+var3
            if current != 0:
                #print("{} (N/A - no previous measurement)".format(total))
                if total > current:
                    #print("{} (increased)".format(total))
                    increase += 1
                elif total < current:
                    #print("{} (decreased)".format(total))
                    decrease += 1
                else:
                    same += 1
            starting_index += 1
            current = total
        except IndexError:
            print("Results: ")
            print("Increases: [{}] \nDecreases: [{}] \nSame Depth: [{}]\n".format(increase, decrease, same))
            loop = False

def main():
    depths = AdventUtils.get_data_from_file('depths.txt') #Add depths here
    depth_changes(depths)

    sliding_window(depths)

main()
