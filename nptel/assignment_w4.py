# cornercase
# : what if the list is empty



def frequency(l):

    # sort the list

    l.sort()
    print(l)
    listmax = []
    element_frequency = 1   # every element occurs at least once 
    max_frequency = 1   # max frequency cant;t be zero if there is at least one element

    for address in range (1,len(l)):
        

        if l[address] == l[address-1]:      # check if the element before it was the same

            element_frequency += 1

            # dont reset right now because then we will loose the progress
        else:
            # only reset when the current progress i.e, continous same element is no longer true, i mean if it is not true than there must be a new element , so element_frequency is 1. Not zero, mind you element exists

            if element_frequency > max_frequency:
                max_frequency = element_frequency

                listmax = [l[address-1]]

            elif element_frequency == max_frequency:

                listmax.append(l[address-1])


            # here if the maximum frequency is less than the current element than obviously this element is occuring more than previously known, so this is the new max frequency 

            # if a new max frequency is encountered, we no longer need the previous element stored in the listMax coz we got a new element, what if the frequency we get is the same as the maximum frequency we got before this, that both the elements have same power so no need to overwrite we get put the new element beside the previous element which also occured exactly te same amount of time this one occured
            
            element_frequency = 1

            # now we can reset this value, as explained in line: 21, at this point, we are running this else part, only because the current elements frequency has ended and we encountered a new element, so we start counting again from 1, not 0 though.
        


    return listmax


print(frequency([13,11,11,12,11,13,14,13,7,11,13,14,14,12,14]))


