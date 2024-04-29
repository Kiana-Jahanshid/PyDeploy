import time 
import random


def marriage(name):

    rand = random.randint(0,10) # how many year later child get married ?
    # 0 = means that child marry now  / 10 = means 10 years later he/she will get married 
    time.sleep(rand) # compute marriage function duration time 
    print(f"{name} married after {rand} years")



def main():
    # for each child , marriage function will be called
    for child in ["child_1" , "child_2" , "child_3" , "child_4"] :
        marriage(child)




if __name__ == "__main__" :

    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    duration_of_main_function = end_time - start_time
    print(f"executed in {duration_of_main_function} seconds ")