def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    # YOUR CODE HERE
    # check validity of arguments
    if unit_in != "c" and unit_in != "f":
        return f"Invalid unit {unit_in}."
    if unit_out != "c" and unit_out != "f":
        return f"Invalid unit {unit_out}."
    if type(temp) is not int and type(temp) is not float:
        return "Invalid temp type (must be int or float)."

    # if unit_in = unit_out, return temp
    if unit_in == unit_out:
        return temp

    # if unit_in = "c", use formula: F = 1.8C + 32
    # else use formula: C = (F - 32) / 1.8
    if unit_in == "c":
        F = 1.8 * temp + 32
        return F
    C = (temp - 32) / 1.8
    return C

print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")
print("c", "f", "zero", convert_temp("c", "f", "zero"), "should be Invalid temp type (must be int or float).")

