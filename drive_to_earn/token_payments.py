import sys
import os
args = sys.argv

if __name__ == '__main__':
    driver_pk = args[1]
    mint_authority = args[2]
    
    os.system('spl-token transfer --allow-unfunded-recipient --fund-recipient {} 1 {}'.format(mint_authority, driver_pk))


    