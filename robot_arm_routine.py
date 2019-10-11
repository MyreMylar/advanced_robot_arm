# -----------------------------------------------------------------------------------------
# Challenge
# ----------
#
# Create a routine for the arm that will stack the three cubes on
# top of the target. Remember - you will need to make sure that you don't
# knock any of them over in the real world!
#
# Useful commands:
#
# - arm.move_to(x,y,z) : moves the arm to the chosen position
# - arm.activate_gripper() : activates the suction gripper picking up a cube
# - arm.deactivate_gripper() : turns off the suction gripper dropping any held cubes
#
# Hints
#
# * You may find that the simulator does not match the real arm's movement range perfectly!
#   This is the fault of the simulator's rubbish code.
# * The given position of the cubes is their centre. You want to pick them up from the top
#   at z=30.
# * If you lift the cubes up to a height above the stack before moving the cubes into
#   position you are less likely to knock it over.
#
# AT THE END:
#
# We will try and get the code from your computer to the raspberry pi the arm is using
# by pasting your code into a pastebin website. Try this link:
#
# - https://pastebin.com/
#
# Paste your code in the box and create a new paste. Then get me to come over to write down the link.
#
# Alternatives:
# - http://www.pastie.org/
# - http://pasted.co/
# -----------------
# Bonus Challenge
# -----------------
#
# Unstack all the stacked cubes back to their original position, then use a loop to repeat the
# routine three times.
# ------------------------------------------------------------------------------------------


def robot_arm_routine(arm):

    arm.move_to(200, 0, 100)
