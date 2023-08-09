from random import randint


def coin_flip(k, side):
    # "H" = 0, "T" = 1
    if (k >= 0) and side in ("H", "T"):
        temp_k = k
        tgt = 0
        final_opt = ""
        if side == "H":
            tgt = 0
        else:
            tgt = 1

        def get_coin_side(int_val):
            if int_val == 0:
                return "H"
            else:
                return "T"

        while temp_k != 0:
            tossed = randint(0, 1)
            if tossed == tgt:
                temp_k = temp_k - 1
                final_opt = final_opt + " " + str(get_coin_side(tossed))
            else:
                temp_k = k
                final_opt = final_opt + " " + str(get_coin_side(tossed))
        print(final_opt)
        print(f"You got {side} {k} times in a row!")
    else:
        print("ERROR!")


coin_flip(7, "T")





