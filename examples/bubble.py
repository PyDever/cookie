
import cookie

def bubble(badList):
    length = len(badList) - 1
    unsorted = True
    while unsorted:
        unsorted = False
        for element in range(0,length):
            #unsorted = False
            if badList[element] > badList[element + 1]:
                 hold = badList[element + 1]
                 badList[element + 1] = badList[element]
                 badList[element] = hold
                 unsorted = True
                 #print badList
             #else:
                 #unsorted = True

    return badList

@cookie.cookie
def main (numbers = None):
    if not numbers == None:
        new_numbers = []
        numbers = numbers.split(',')
        for number in numbers:
            number = int(number)
            new_numbers.append(number)
        print(bubble(new_numbers))

if __name__ == "__main__":
    main()

