from utils.brick import Motor
import time
other_motor1 = Motor("A")
other_motor2 = Motor("B")

  #Test motor port A and motor port B

# Designates to Encoder, that the current physical position is 0 degrees
other_motor1.reset_encoder()
other_motor2.reset_encoder()


# Rotate to position that is 720 degrees away from the 0 position
other_motor1.set_position_relative(-540)
other_motor2.set_position_relative(-540) # This does nothing, because we are here
time.sleep(3) # Wait to finish

other_motor1.set_position_relative(540)
other_motor2.set_position_relative(540)
time.sleep(3)

# other_motor1.set_position(720) # This does nothing, because we are here
# other_motor2.set_position(720)
# time.sleep(0.5) # Wait to finish
# 
# 
# other_motor1.set_position(700) # Move backwards 20 degrees
# other_motor2.set_position(700) # Move backwards 20 degrees
# 
# time.sleep(2)
# 
# # Returns the current position for you. So you know where you are.
# print(other_motor1.get_position())
# print(other_motor2.get_position())
# 
# 
# 
# # Prevents position control from going over either:
# # 50% power or 90 deg/sec, whichever is slower
# other_motor1.set_limits(power=50, dps=90)
# other_motor2.set_limits(power=50, dps=90)
# 
# 
# other_motor1.set_limits(power=50) # Limit one only, don't care about other
# other_motor1.set_limits() # UNLIMITED POWER (AND SPEED)
# 
# other_motor2.set_limits(power=50) # Limit one only, don't care about other
# other_motor2.set_limits() # UNLIMITED POWER (AND SPEED)
# 
# # Will rotate 180 degrees backwards from current position.
# # Does not care about the absolute position.
# other_motor1.set_position_relative(-180)
# other_motor2.set_position_relative(-180)
# time.sleep(2)
