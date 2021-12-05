import AdventUtils

# Part one
def drive_the_sub(movements):
    print('Running part one...')
    horizontalPosition = 0
    depth = 0

    # For each command, need to split into the command word and the value
    for movement in movements:
        commandAndValue = movement.split()
        command = commandAndValue[0]
        value = int(commandAndValue[1])

        if command == 'forward':
            horizontalPosition += value
        elif command == 'down':
            depth += value
        elif command == 'up':
            depth -= value
        else:
            print('Invalid command word')

    print('Horizontal Position: [{}]'.format(horizontalPosition))
    print('Depth: [{}]'.format(depth))
    print('Multiplied: [{}]\n'.format(horizontalPosition * depth))

# Part two
def drive_with_aim(movements):
    print('Running part two, adding a value for aim...')
    horizontalPosition = 0
    depth = 0
    aim = 0

    # For each command, need to split into the command word and the value
    for movement in movements:
        commandAndValue = movement.split()
        command = commandAndValue[0]
        value = int(commandAndValue[1])

        if command == 'forward':
            horizontalPosition += value
            depth += (aim * value)
        elif command == 'down':
            aim += value
        elif command == 'up':
            aim -= value
        else:
            print('Invalid command word')

    print('Horizontal Position: [{}]'.format(horizontalPosition))
    print('Depth: [{}]'.format(depth))
    print('Multiplied: [{}]'.format(horizontalPosition * depth))

def main():
    data = AdventUtils.get_data_from_file('drive.txt')
    drive_the_sub(data)
    drive_with_aim(data)

main()
