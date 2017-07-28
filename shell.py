import time
import core
import disk

def main():
    print("\t\tWelcome to AZ's Canopy Party Tents Rental!\n")
    time.sleep(.5)
    print("Canopy tents are a light weight structure, they are great for protection from sun or light rain. They are to be installed and removed by you, the renter.\n")
    time.sleep(5)
    tent = input('Canopy tents are available to rent up to 2 days. Would you like to rent a tent or tents today? 1: yes 2: no\n')
    if tent == '2' or tent.lower() == 'no':
        print("That's fine, come back again if you change your mind!")
     
    elif tent == '1' or tent.lower() == 'yes':
            print('\nGreat, here are the tent sizes we have available. You can choose to just rent the tent or have chairs and tables included with them.\n')
            print('\n'.join(core.type_of_tents()))
            tent1 = input('Tent: \n')
            not1 = core.cost_of_tents(tent1)
            if not disk.take_away(tent1, not1):
                print('sorry')
                return None
            tents = core.cost_of_tents(tent1)
            con = input('\nTent ' + tent1 + ' price is $' + str(tents) + ' dollars. Would you like to continue?\n')
            tent2 = core.deposit(tents)
            tent3 = core.total(tents)
            tent4 = tents * 2
            if con == 'yes':
                days = input('\nHow many days will you be renting this? Only up to 2 days.\n')
                total = (float(tent2) + float(tent3)) + float(tents)
                total2 = (float(tent2) + float(tent3)) + float(tent4)
                if days == '1':
                    print('Your renting this for 1 day, your total with deposit and tax is $' + str(float(total)))
                    history = disk.keep_history(tent1, total)
                    print('Thank you')
                elif days == '2':
                    print('\nYour renting this for 2 day, your total with deposit and tax is $' + str(float(total2)))
                    history = disk.keep_history(tent1, total2)
                    print('Thank you')
                    

        



    








if __name__ == '__main__':
    main() 