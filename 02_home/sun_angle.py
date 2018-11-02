"""
Your task is to find the angle of the sun above the horizon knowing the time of the day. 
Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees. 
At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees. 
6:00 PM is the time of the sunset so the angle is 180 degrees. 
If the input will be the time of the night (before 6:00 AM or after 6:00 PM), 
your function should return - "I don't see the sun!".
Example:
	sun_angle("07:00") == 15
	sun_angle("12:15"] == 93.75
	sun_angle("01:23") == "I don't see the sun!"
"""

def sun_angle(time):
    #replace this for solution
    hour, minute = list(map(int,time.split(':')))
    if hour < 6 or hour > 18 or (hour == 18 and minute > 0):
        return "I don't see the sun!"
    return hour * 15 + minute * 1/4 - 90

def sun_angle_v2(time):
    h, m = list(map(int, time.split(':')))
    angle = 15 * h + m / 4 - 90
    return angle if 0 <= angle <= 180 else "I don't see the sun!"

def sun_angle_3(time):
    hours = int(time[:2]) + int(time[3:]) / 60
    if (hours < 6) or (hours > 18):
        return "I don't see the sun!"
    else:
        return (hours - 6)/12 * 180

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")